![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 3 - Telegram Integration

This step covers creating a Telegram bot, connecting it to OpenClaw,
and setting up a personal channel for receiving daily job digests.

---

## What is Telegram used for here?

Telegram is the communication layer of the agent.
Every day at 20:00 the agent sends a ranked list of job listings
directly to your personal Telegram channel.

---

## Creating a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send the command: `/newbot`
3. Choose a name: e.g. `Job Hunting Agent`
4. Choose a username: e.g. `jobhunting_silvio_bot`
5. BotFather will return your **Bot Token** — save it

---

## Creating a Personal Channel

1. In Telegram click **New Channel**
2. Set it to **Private**
3. Name it e.g. `Job Digest`
4. Add your bot as **Administrator** to the channel

---

## Getting Your Channel ID

1. Forward any message from your channel to **@userinfobot**
2. It will return your Channel ID (starts with -100...)
3. Save this ID

---

## Adding Telegram to OpenClaw

Edit your OpenClaw config file:
```bash
nano ~/.openclaw/config.yaml
```

Add Telegram credentials:
```yaml
telegram:
  bot_token: YOUR_BOT_TOKEN
  channel_id: YOUR_CHANNEL_ID
```

---

## Test the Connection

```bash
openclaw test telegram
```

Expected output:
✓ Telegram bot connected
✓ Message sent to channel
Check your Telegram channel — you should see a test message.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot not sending messages | Check bot is Admin in channel |
| Wrong channel ID | Use @userinfobot to verify |
| Token invalid | Regenerate via @BotFather |

---

## Next Step

[Step 4 - Perplexity + Firecrawl Integration](./STEP4-Perplexity-Firecrawl.md)
