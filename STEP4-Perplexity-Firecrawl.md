![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 4 - Perplexity + Firecrawl Integration

This step covers connecting two research tools to the agent:
Perplexity for live web search and Firecrawl for scraping 
job boards that use JavaScript protection.

---

## Why Two Tools?

| Tool | What it does | Why we need it |
|------|-------------|----------------|
| Perplexity | Live web search | Finds fresh job listings in real time |
| Firecrawl | JS-protected scraping | Bypasses LinkedIn, MojPosao rendering |

Perplexity finds the jobs. Firecrawl extracts the full details.

---

## Perplexity Setup

### Getting Your API Key
1. Go to: https://perplexity.ai
2. Navigate to **Settings** → **API**
3. Click **"Generate API Key"**
4. Copy and save the key

> I have Perplexity Pro active until 01.2027 — API access is included.

### Adding to OpenClaw
```yaml
perplexity:
  api_key: YOUR_PERPLEXITY_API_KEY
  search_depth: detailed
```

### Test
```bash
openclaw test perplexity
```

Expected output:
```
✓ Perplexity connected
✓ Search returning results
```

---

## Firecrawl Setup

### Getting Your API Key
1. Go to: https://firecrawl.dev
2. Create an account
3. Navigate to **Dashboard** → **API Keys**
4. Copy your key

### Adding to OpenClaw
```yaml
firecrawl:
  api_key: YOUR_FIRECRAWL_API_KEY
```

### Test
```bash
openclaw test firecrawl
```

Expected output:
```
✓ Firecrawl connected
✓ Scraping engine ready
```

---

## How They Work Together

```
Perplexity → finds job listing URLs
     ↓
Firecrawl → scrapes full job description
     ↓
Gemini → reads and scores the listing
     ↓
Telegram → sends digest to you
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Perplexity returning no results | Check API key, verify Pro is active |
| Firecrawl blocked | Some sites block scrapers — use rotation |
| Slow scraping | Normal for JS-heavy sites like LinkedIn |

---

## Next Step

[Step 5 - Job Scoring System](./STEP5-Job-Scoring.md)
