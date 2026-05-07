![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 2 - Gemini API Configuration

This step covers setting up Gemini 2.5 Flash as the AI brain 
of the agent — responsible for reasoning, decision making, 
and job scoring.

---

## What is Gemini 2.5 Flash?

Gemini 2.5 Flash is Google's fast and cost-efficient AI model.
In this project it acts as the central brain — it reads job listings,
compares them to your CV, and decides which ones are worth applying for.

---

## Getting Your API Key

1. Go to: https://aistudio.google.com
2. Sign in with your Google account
3. Click **"Get API Key"** → **"Create API key"**
4. Copy the key and store it safely

---

## Setting a Spend Cap

To avoid unexpected charges, set a monthly spend cap:

1. Go to: https://console.cloud.google.com
2. Navigate to **Billing** → **Budgets & alerts**
3. Create a budget: £4/month
4. Enable alerts at 50%, 90%, 100%

---

## Adding Key to OpenClaw

Edit your OpenClaw config file:
```bash
nano ~/.openclaw/config.yaml
```

Add your key:
```yaml
model:
  provider: google
  name: gemini-2.5-flash
  api_key: YOUR_GEMINI_API_KEY
```

---

## Test the Connection

```bash
openclaw test gemini
✓ Gemini 2.5 Flash connected
✓ Model responding
---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Invalid API key | Regenerate key in AI Studio |
| Quota exceeded | Check spend cap in Cloud Console |
| Slow responses | Normal — Flash optimises for cost |

---

## Next Step

[Step 3 - Telegram Integration](./STEP3-Telegram-Integration.md)
```

Expected output:
