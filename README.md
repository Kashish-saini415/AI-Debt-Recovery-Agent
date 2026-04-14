# Automated AI Debt Recovery Agent

An automated system that identifies pending payments from Airtable, generates personalized professional reminders using Gemini AI, and sends them via Twilio SMS.

## Features
- Airtable integration for data management.
- AI-powered message generation via OpenRouter (Gemini).
- Automated SMS delivery using Twilio.
- Status tracking and automation with Windows Task Scheduler.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your credentials in the `.env` file.
4. Run the agent: `python main.py`