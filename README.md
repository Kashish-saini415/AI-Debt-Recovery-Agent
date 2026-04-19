Automated AI Debt Recovery Agent (Voice Edition)
An advanced automated system that identifies pending payments from Airtable, initiates personalized Voice Calls using Twilio, and engages in natural, Multilingual conversations powered by ElevenLabs AI.

🚀 Key Features
Smart Data Management: Seamless integration with Airtable to track customer records and payment status.

Multilingual AI Voice: Integration with ElevenLabs (Multilingual v2), allowing the agent to communicate naturally in Hindi, English, and other regional languages.

Automated Voice Calls: Utilizes Twilio Voice API to trigger calls automatically when a record is marked as "Pending".

Human-in-the-Loop (Manager Transfer): Advanced logic to detect "Urgent" cases and automatically transfer the call to a human manager.

Real-time Processing: Bridge established between local development environments and cloud APIs for instantaneous execution.

🛠️ Tech Stack
Language: Python 3.x

Database: Airtable

Communication: Twilio Voice API

AI Voice: ElevenLabs (Conversational AI)

Environment: Python-dotenv, VS Code

📋 Setup & Installation
Clone the Repository:

Bash
git clone https://github.com/Kashish-saini415/Kashish-saini415.git
cd Kashish-saini415
Install Dependencies:

Bash
pip install airtable-python-wrapper twilio python-dotenv
Configuration:
Create a .env file in the root directory and add your credentials:

Plaintext
AIRTABLE_API_KEY=your_airtable_key
AIRTABLE_BASE_ID=your_base_id
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
ELEVENLABS_AGENT_ID=your_agent_id
MANAGER_PHONE_NUMBER=your_manager_number
Run the Agent:

Bash
python main.py
🔄 Workflow
The script scans the Airtable for records with the status 'Pending'.

If a record is found, it triggers a Twilio call to the customer's phone number.

Upon connection, the ElevenLabs AI Agent takes over the conversation using a natural, human-like voice.

If the status is marked as 'Urgent', the system bypasses the AI and routes the call directly to the Manager.
