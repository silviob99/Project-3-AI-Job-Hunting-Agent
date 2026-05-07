from __future__ import annotations

import json
import re
from pathlib import Path

INPUT_FILE = Path.home() / "job-hunter" / "data" / "reed_jobs_multi.json"
OUTPUT_FILE = Path.home() / "job-hunter" / "data" / "reed_jobs_multi_filtered.json"

SENIOR_PATTERNS = [
    r"\bsenior\b",
    r"\blead\b",
    r"\bmanager\b",
    r"\bprincipal\b",
    r"\bhead\b",
    r"\bshift lead\b",
    r"\bl2\b",
    r"\bl3\b",
    r"\bt2\b",
]

GOOD_PATTERNS = [
    r"\bsoc analyst\b",
    r"\bsecurity analyst\b",
    r"\bcyber security analyst\b",
    r"\bcyber analyst\b",
    r"\bincident response analyst\b",
    r"\biam analyst\b",
]

SKILL_BONUS_PATTERNS = [
    r"\bsentinel\b",
    r"\bdefender\b",
    r"\bkql\b",
    r"\bsiem\b",
    r"\bentra\b",
    r"\bincident response\b",
    r"\bsecops\b",
]

BAD_TITLE_PATTERNS = [
    r"training course",
    r"hide all",
]

def matches_any(patterns: list[str], text: str) -> bool:
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)

def score_job(job: dict) -> int:
    text = " ".join([
        job.get("title", ""),
        job.get("summary", ""),
        job.get("company", ""),
        job.get("location", ""),
    ])

    score = 0

    if matches_any(GOOD_PATTERNS, text):
        score += 5

    if "junior" in text.lower() or "t1" in text.lower() or "entry" in text.lower():
        score += 3

    if matches_any(SKILL_BONUS_PATTERNS, text):
        score += 2

    if "london" in text.lower():
        score += 1

    return score

def classify(job: dict) -> str:
    title = job.get("title", "")

    if matches_any(BAD_TITLE_PATTERNS, title):
        return "reject"

    if matches_any(SENIOR_PATTERNS, title):
        return "reject"

    score = score_job(job)

    if score >= 7:
        return "strong"
    if score >= 4:
        return "possible"
    return "reject"

def main() -> None:
    jobs = json.loads(INPUT_FILE.read_text(encoding="utf-8"))

    results = []
    for job in jobs:
        category = classify(job)
        if category == "reject":
            continue

        job["score"] = score_job(job)
        job["category"] = category
        results.append(job)

    results.sort(key=lambda x: x["score"], reverse=True)

    OUTPUT_FILE.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Saved {len(results)} filtered jobs to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
