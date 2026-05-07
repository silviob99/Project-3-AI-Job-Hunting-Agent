![AI-Job-Agent-Banner](./assets/AI-Job-Hunter.png)
# Step 5 - Job Scoring System

This step covers how the agent compares job listings against 
your CV and assigns a compatibility score from 1 to 10.

---

## How Scoring Works

Gemini reads each job listing and compares it to your CV.
It returns a structured score with reasoning.

```
Job Listing + CV → Gemini → Score (1-10) + Reasoning
```

---

## Scoring Criteria

| Category | Weight | Description |
|----------|--------|-------------|
| Skills match | 40% | Do your skills match requirements? |
| Experience level | 25% | Junior/Mid/Senior alignment |
| Location/Remote | 20% | On-site vs remote preference |
| Salary range | 15% | Within expected range |

---

## CV Setup

Store your CV as a plain text file that Gemini can read:

```bash
~/.openclaw/cv.txt
```

Example format:
```
Name: Silvio Banfic
Role: Junior SOC Analyst / Cloud Security
Skills: Azure, AWS, Microsoft Defender, KQL, SIEM, Linux
Certifications: AWS Solutions Architect, Security+
Experience: 2 years infrastructure, transitioning to security
Location: London (open to remote)
```

---

## Scoring Prompt

OpenClaw sends this prompt to Gemini for each listing:

```
Given this CV: [cv.txt]
And this job listing: [scraped listing]

Score the compatibility from 1-10.
Return JSON:
{
  "score": 8,
  "title": "SOC Analyst - London",
  "company": "CrowdStrike",
  "reason": "Strong Azure and SIEM match. Missing CrowdStrike experience.",
  "apply": true
}
```

---

## Score Thresholds

| Score | Action |
|-------|--------|
| 8-10 | ✅ Included in daily digest |
| 5-7 | ⚠️ Included with warning |
| 1-4 | ❌ Filtered out silently |

---

## Example Telegram Output

```
🔍 Daily Job Digest — 07.05.2026

1. SOC Analyst @ CrowdStrike ⭐ 9/10
   London | £45-55k | Remote hybrid
   ✅ Strong Azure + SIEM match

2. Security Engineer @ HSBC ⭐ 7/10
   London | £50k | On-site
   ⚠️ Good fit but requires 3yr experience

3. Cloud Security Analyst @ NHS ⭐ 8/10
   Remote | £40k
   ✅ AWS + Linux match

Total: 3 new listings today
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| All scores too low | Update cv.txt with more keywords |
| No listings passing threshold | Lower threshold temporarily |
| Gemini returning wrong format | Tighten JSON prompt |

---

## Next Step

[Step 6 - Gmail Integration](./STEP6-Gmail.md)
