![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 1 - OpenClaw Gateway Setup

This step covers installing OpenClaw, starting the gateway, 
and verifying the connection is active.

---

## What is OpenClaw?

OpenClaw is an agent orchestration platform that connects AI models 
(Gemini, GPT, local LLMs) with external tools and communication 
channels like Telegram.

---

## Installation

Download and install OpenClaw from the official website:
https://openclaw.io

Verify installation:
```bash
openclaw --version
```

---

## Starting the Gateway


```bash
openclaw gateway start
```

Expected output:
Gateway running on port 8080
Connected to agent runtime
---

## Configuration

OpenClaw uses a config file located at:
~/.openclaw/config.yaml
Set your Gemini API key:
```yaml
model:
  provider: google
  name: gemini-2.5-flash
  api_key: YOUR_GEMINI_API_KEY
```

---

## Verify Gateway is Running

```bash
openclaw gateway status
```

---

## Troubleshooting

| Problem | Solution |
|---------|---------|
| Port already in use | `openclaw gateway stop` then start again |
| API key error | Double-check key in config.yaml |
| No internet | Check VPN kill switch (ProtonVPN) |

---

## Next Step

[Step 2 - Gemini API Configuration](./STEP2-Gemini-API-Configuration.md)
