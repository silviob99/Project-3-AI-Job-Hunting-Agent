# Project-3-AI-Job-Hunting-Agent

An autonomous AI agent that searches for jobs daily, scores them against 
your CV, tracks applications, and delivers results via Telegram.

## Table of Contents
- Project Overview
- Architecture
- Prerequisites
- Steps
- Roadmap

### Project Overview

Project-3: AI Job Hunting Agent is a multi-component AI pipeline built 
on OpenClaw, Gemini 2.5 Flash, and Telegram. The agent runs daily at 20:00, 
scrapes job boards, scores listings against a personal CV, and sends 
a ranked digest. It tracks applications, sends follow-up reminders after 
7 days, and sorts job-related emails in Gmail.

### Architecture

| Component     | Role                        |
|---------------|-----------------------------|
| Gemini 2.5    | Brain — reasoning & scoring |
| Perplexity    | Live web search             |
| Firecrawl     | JS-protected scraping       |
| Telegram      | Daily digest delivery       |
| Gmail         | Email sorting               |
| OpenClaw      | Agent orchestration         |

### Prerequisites
- Mac with OpenClaw installed
- Gemini API key
- Telegram Bot token
- Perplexity Pro account
- Firecrawl API key

### Steps

- Step 0: [Prerequisites](./STEP0-Prerequisites.md)
- Step 1: [OpenClaw Gateway Setup](./STEP1-OpenClaw-Gateway-Setup.md)
- Step 2: [Gemini API Configuration](./STEP2-Gemini-API-Configuration.md)
- Step 3: [Telegram Integration](./STEP3-Telegram-Integration.md)
- Step 4: [Perplexity + Firecrawl](./STEP4-Perplexity-Firecrawl.md)
- Step 5: [Job Scoring System](./STEP5-Job-Scoring.md)
- Step 6: [Gmail Integration](./STEP6-Gmail.md)
- Step 7: [VPS Deployment](./STEP7-VPS-Deployment.md)

### Roadmap
- [x] OpenClaw + Gemini + Telegram
- [ ] Perplexity live search
- [ ] Firecrawl scraping
- [ ] CV scoring algorithm
- [ ] Gmail sorting
- [ ] Hetzner VPS 24/7
