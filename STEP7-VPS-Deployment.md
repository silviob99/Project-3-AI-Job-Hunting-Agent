![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 7 - VPS Deployment

This step covers moving the agent from your Mac to a Hetzner 
VPS so it runs 24/7 without needing your laptop to be on.

---

## Why a VPS?

| Mac | VPS |
|-----|-----|
| Must be on and awake | Runs 24/7 |
| Tied to your location | Always online |
| Uses your battery | ~£4/month |
| Stops when you close lid | Never stops |

---

## Choosing a Hetzner Plan

1. Go to: https://hetzner.com/cloud
2. Create an account
3. Choose server:

| Plan | CPU | RAM | Price |
|------|-----|-----|-------|
| CX22 | 2 vCPU | 4GB | ~£4/mo ✅ |
| CX32 | 4 vCPU | 8GB | ~£8/mo |

**CX22 is enough for this agent.**

4. Choose OS: **Ubuntu 24.04**
5. Choose location: **Falkenstein** or **Helsinki**
6. Add your SSH key
7. Click **Create & Buy**

---

## Connecting to Your VPS

```bash
ssh root@YOUR_VPS_IP
```

---

## Server Setup

Update the system:
```bash
apt update && apt upgrade -y
```

Install required tools:
```bash
apt install -y git curl wget nano
```

---

## Installing OpenClaw on VPS

```bash
curl -fsSL https://openclaw.io/install.sh | bash
```

Verify:
```bash
openclaw --version
```

---

## Transferring Your Config

Copy your local config to VPS:
```bash
scp ~/.openclaw/config.yaml root@YOUR_VPS_IP:~/.openclaw/
scp ~/.openclaw/cv.txt root@YOUR_VPS_IP:~/.openclaw/
scp ~/.openclaw/gmail-credentials.json root@YOUR_VPS_IP:~/.openclaw/
```

---

## Running Agent 24/7 with systemd

Create a service file:
```bash
nano /etc/systemd/system/openclaw.service
```

Paste this:
```ini
[Unit]
Description=OpenClaw Job Hunting Agent
After=network.target

[Service]
ExecStart=/usr/local/bin/openclaw gateway start
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
systemctl enable openclaw
systemctl start openclaw
systemctl status openclaw
```

---

## Scheduling Daily Digest at 20:00

```bash
crontab -e
```

Add this line:
```
0 20 * * * openclaw agent run job-digest
```

---

## Verify Everything Works

```bash
openclaw status
```

Expected output:
```
✓ Gateway running
✓ Gemini connected
✓ Telegram connected
✓ Gmail connected
✓ Scheduler active — next run: 20:00
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| SSH connection refused | Check Hetzner firewall rules |
| Service not starting | Check `journalctl -u openclaw` |
| Agent not running at 20:00 | Verify crontab timezone |

---

## You're Done! 🎉

Your AI Job Hunting Agent is now running 24/7.

Every day at 20:00 you will receive:
- 4-5 scored job listings on Telegram
- Gmail automatically sorted
- Follow-up reminders after 7 days
