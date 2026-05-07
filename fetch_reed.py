from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.reed.co.uk/jobs"
OUTPUT_DIR = Path.home() / "job-hunter" / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "reed_jobs.json"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/146.0.0.0 Safari/537.36"
    )
}


@dataclass
class Job:
    title: str
    company: str
    location: str
    source: str
    url: str
    summary: str


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_reed_jobs(query: str = "soc analyst", location: str = "London") -> List[Job]:
    params = {
        "keywords": query,
        "location": location,
    }

    response = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    jobs: List[Job] = []

    # NOTE:
    # Reed HTML can change. These selectors are a practical starter and may need tweaking.
    cards = soup.select("article, .job-result, .job-card, [data-qa='job-card']")

    seen_urls = set()

    for card in cards:
        link = card.select_one("a[href*='/jobs/']")
        if not link:
            continue

        href = link.get("href", "").strip()
        if not href:
            continue

        if href.startswith("/"):
            url = f"https://www.reed.co.uk{href}"
        else:
            url = href

        if url in seen_urls:
            continue
        seen_urls.add(url)

        title = clean_text(link.get_text(" ", strip=True))

        company_el = (
            card.select_one("[data-qa='company-name']")
            or card.select_one(".company")
            or card.select_one(".gtmJobListingPostedBy")
        )
        location_el = (
            card.select_one("[data-qa='job-metadata-location']")
            or card.select_one(".location")
            or card.select_one(".gtmJobListingLocation")
        )
        summary_el = (
            card.select_one("[data-qa='job-description']")
            or card.select_one(".description")
            or card.select_one("p")
        )

        company = clean_text(company_el.get_text(" ", strip=True)) if company_el else "Unknown"
        location_text = clean_text(location_el.get_text(" ", strip=True)) if location_el else "Unknown"
        summary = clean_text(summary_el.get_text(" ", strip=True)) if summary_el else ""

        if not title:
            continue

        jobs.append(
            Job(
                title=title,
                company=company,
                location=location_text,
                source="Reed",
                url=url,
                summary=summary,
            )
        )

    return jobs


def save_jobs(jobs: List[Job]) -> None:
    OUTPUT_FILE.write_text(
        json.dumps([asdict(job) for job in jobs], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


if __name__ == "__main__":
    jobs = fetch_reed_jobs(query="soc analyst", location="London")
    save_jobs(jobs)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")
