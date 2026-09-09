# Daily Standup Summarizer Agent

An AI agent that turns your messy work notes into a clean, structured daily standup update in seconds.

## What it does

Paste your raw notes or brain dump, and the agent formats it into a professional standup with:
- ✅ **Done** — what you completed
- 🔄 **Doing** — what you're working on today
- 🚧 **Blockers** — anything blocking your progress

## Who it's for

Developers, project managers, and any professional who does daily standups and wastes time formatting their notes every morning.

## How it works

Built with the [Strands Agents SDK](https://strandsagents.com) and AWS Bedrock (Amazon Nova). The agent uses two tools:

- `summarize_notes` — extracts key points from unstructured input
- `format_standup` — structures the output into a clean standup report

The model reasons through your input, decides which tools to call, and returns a formatted standup automatically.

## Setup

**Prerequisites:**
- Python 3.10+
- AWS account with Bedrock access enabled
- AWS credentials configured (`aws configure`)

**Install:**
```bash
pip install -r requirements.txt
```

**Run:**
```bash
python agent.py
```

## Example

**Input:**
```
yesterday i fixed the login bug and reviewed john's PR, today working on the payment API,
also need to update the docs. waiting on design team for the new mockups
```

**Output:**
```
📋 Daily Standup

✅ Done:
• Fixed login bug
• Reviewed John's PR

🔄 Doing:
• Working on payment API
• Updating documentation

🚧 Blockers:
• Waiting on design team for new mockups
```

## Track

**Professional Agents** — handles a repetitive daily work task automatically.

## Built with

- [Strands Agents SDK](https://strandsagents.com)
- AWS Bedrock (Amazon Nova Pro)
