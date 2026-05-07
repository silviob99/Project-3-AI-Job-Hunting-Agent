![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)

# Project-3-AI-Job-Hunting-Agent

An autonomous Python pipeline that scrapes job boards daily, scores 
listings against a target profile, and delivers ranked results via Telegram.

## Table of Contents
- [Project Overview](#project-overview)
- [Current Implementation](#current-implementation)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Scripts](#scripts)
- [Roadmap](#roadmap)

## Project Overview

A self-built job hunting automation tool that eliminates manual job searching.
The pipeline fetches listings from Reed.co.uk, filters out senior/irrelevant 
roles, scores matches based on keywords and location, and sends a ranked 
digest to Telegram every day.

Built as a learning project to develop Python automation, API integration, 
and scripting skills — directly applicable to security automation workflows 
in SOC environments.

## Current Implementation

| Component | Role |
|---|---|
| Python + BeautifulSoup | Scrapes Reed.co.uk job listings |
| Custom scoring logic | Filters and ranks jobs by relevance |
| Telegram Bot API | Delivers daily digest |
| JSON storage | Stores and deduplicates results |

## Prerequisites
- Python 3.x
- pip packages: `requests`, `beautifulsoup4`, `lxml`
- Telegram Bot token
- Telegram Chat ID

## Scripts

| Script | Description |
|---|---|
| `fetch_reed.py` | Scrapes Reed.co.uk for a single query |
| `fetch_reed_multi.py` | Scrapes multiple job categories, deduplicates |
| `filter_score_reed.py` | Scores and filters jobs by seniority/keywords |
| `send_top_jobs_telegram.py` | Sends top results to Telegram |

## Roadmap
- [x] Python scraping pipeline (Reed.co.uk)
- [x] Multi-query fetching with deduplication
- [x] Keyword scoring and seniority filtering
- [x] Telegram delivery
- [ ] Gemini AI scoring against CV
- [ ] Perplexity live web search
- [ ] Gmail sorting integration
- [ ] Hetzner VPS 24/7 deployment
