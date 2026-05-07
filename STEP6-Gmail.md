![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 6 - Gmail Integration

This step covers connecting Gmail to the agent for automatic 
sorting of job-related emails into dedicated folders.

---

## What Gmail is Used for Here

When you start applying for jobs, your inbox fills up fast.
The agent automatically sorts:

| Email Type | Where it goes |
|------------|--------------|
| Application confirmations | 📁 Jobs/Applied |
| Interview invitations | 📁 Jobs/Interviews |
| Rejections | 📁 Jobs/Rejections |
| Follow-up reminders | 📁 Jobs/Follow-up |

---

## Gmail API Setup

### Enable Gmail API
1. Go to: https://console.cloud.google.com
2. Search for **Gmail API** → Click **Enable**
3. Navigate to **Credentials** → **Create Credentials**
4. Choose **OAuth 2.0 Client ID**
5. Download the `credentials.json` file

### Store Credentials
```bash
~/.openclaw/gmail-credentials.json
```

---

## Adding Gmail to OpenClaw

Edit your OpenClaw config file:
```bash
nano ~/.openclaw/config.yaml
```

Add Gmail config:
```yaml
gmail:
  credentials_file: ~/.openclaw/gmail-credentials.json
  labels:
    applied: "Jobs/Applied"
    interviews: "Jobs/Interviews"
    rejections: "Jobs/Rejections"
    followup: "Jobs/Follow-up"
```

---

## Creating Gmail Labels

1. Open Gmail
2. On the left sidebar scroll down → **Create new label**
3. Create these labels:
   - `Jobs/Applied`
   - `Jobs/Interviews`
   - `Jobs/Rejections`
   - `Jobs/Follow-up`

---

## How Sorting Works

Gemini reads incoming emails and classifies them:

```
New email arrives → Gemini reads subject + sender
       ↓
Classifies as: application / interview / rejection / other
       ↓
Moves to correct Gmail label automatically
```

---

## Follow-up Reminders

The agent tracks when you applied and sends a Telegram 
reminder after 7 days if no response:

```
⏰ Follow-up Reminder — 14.05.2026

No response from CrowdStrike after 7 days.
Applied: 07.05.2026 — SOC Analyst

Consider following up via LinkedIn.
```

---

## Test the Connection

```bash
openclaw test gmail
```

Expected output:
```
✓ Gmail API connected
✓ Labels found
✓ Sorting rules active
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| OAuth error | Re-download credentials.json |
| Labels not found | Create labels manually in Gmail first |
| Emails not sorting | Check Gemini classification prompt |

---

## Next Step

[Step 7 - VPS Deployment](./STEP7-VPS-Deployment.md)
