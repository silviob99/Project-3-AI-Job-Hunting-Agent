from __future__ import annotations

import json
import os
import textwrap
from pathlib import Path

import requests

INPUT_FILE = Path.home() / "job-hunter" / "data" / "reed_jobs_multi_filtered.json"

# Fill these in with your real values
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

def build_message(jobs: list[dict], limit: int = 5) -> str:
    strong = [j for j in jobs if j.get("category") == "strong"][:limit]
    possible = [j for j in jobs if j.get("category") == "possible"][:limit]

    lines: list[str] = []
    lines.append("💼 Job Hunter Update")
    lines.append("")

    if strong:
        lines.append("🔥 Strong matches")
        for i, job in enumerate(strong, 1):
            lines.append(
                textwrap.dedent(
                    f"""\
                    {i}. {job['title']}
                    Company: {job['company']}
                    Location: {job['location']}
                    Score: {job['score']}/10
                    Source: {job['source']}
                    Link: {job['url']}
                    """
                ).strip()
            )
            lines.append("")

    if possible:
        lines.append("🟡 Possible matches")
        for i, job in enumerate(possible, 1):
            lines.append(
                textwrap.dedent(
                    f"""\
                    {i}. {job['title']}
                    Company: {job['company']}
                    Location: {job['location']}
                    Score: {job['score']}/10
                    Source: {job['source']}
                    Link: {job['url']}
                    """
                ).strip()
            )
            lines.append("")

    if not strong and not possible:
        lines.append("No matching jobs found today.")

    return "\n".join(lines).strip()


def send_telegram_message(bot_token: str, chat_id: str, text: str) -> None:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": True,
        },
        timeout=20,
    )
    response.raise_for_status()


def main() -> None:
    if not BOT_TOKEN or not CHAT_ID:
        raise SystemExit(
            "Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID as environment variables."
        )

    jobs = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    message = build_message(jobs, limit=5)
    send_telegram_message(BOT_TOKEN, CHAT_ID, message)
    print("Sent Telegram message successfully.")


if __name__ == "__main__":
    main()
