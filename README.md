# 🤖 Automated AI Debt Recovery Agent (Voice Edition)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Twilio](https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=Twilio&logoColor=white) 
![Airtable](https://img.shields.io/badge/Airtable-18BFFF?style=for-the-badge&logo=Airtable&logoColor=white) 
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-2D3436?style=for-the-badge&logo=elevenlabs&logoColor=white)

An advanced automation system designed to handle debt recovery calls efficiently. This agent identifies pending records from **Airtable**, initiates automated voice calls via **Twilio**, and engages in natural, **Multilingual conversations** using **ElevenLabs Conversational AI**.

---

## 🚀 Key Features

* **Airtable Integration:** Automatically fetches customer data, phone numbers, and payment status for streamlined management.
* **Multilingual AI Support:** High-fidelity voice conversations in Hindi and English using the ElevenLabs Multilingual v2 model.
* **Automated Calling:** Fully automated outbound calls triggered by real-time status updates in the database.
* **Human-in-the-Loop:** Intelligent escalation logic to detect urgent cases and automatically route calls to a human manager.
* **Error Handling:** Robust indentation and exception handling to ensure continuous script execution.


## 🛠️ Tech Stack & Tools

* **Language:** Python 3.x
* **Database:** Airtable (Cloud-based CRM)
* **Voice API:** Twilio Voice (TwiML & WebSocket Streams)
* **AI Engine:** ElevenLabs (Conversational AI Agent)
* **Environment:** VS Code, Git, Python-dotenv

---

## 📋 Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/Kashish-saini415/Kashish-saini415.git](https://github.com/Kashish-saini415/Kashish-saini415.git)
cd Kashish-saini415
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Required Libraries
```bash
pip install airtable-python-wrapper twilio python-dotenv
```

### 4. Environment Variables Configuration
Create a **.env** file in the root directory and add your credentials (use placeholders for security):
```Plaintext
AIRTABLE_API_KEY=your_airtable_api_key
AIRTABLE_BASE_ID=your_airtable_base_id
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
ELEVENLABS_AGENT_ID=your_elevenlabs_agent_id
MANAGER_PHONE_NUMBER=your_manager_phone_number
```

### 5. Run the Agent
```Bash
python main.py
```

---


## 🔄 Workflow Logic

**1. Data Fetch:** The script scans the Airtable ```Grid view```  for records where ```Status == 'Pending'```.

**2. Trigger Call:** If a record is found, Twilio initiates an outbound call to the customer's phone number.

**3. AI Connection:** Once the call is answered and the trial key-press is cleared, a WebSocket stream connects the call to the **ElevenLabs AI Agent**.

**4. Conversation:** The AI engages in a natural dialogue, providing payment reminders in the user's preferred language.

**5. Escalation:** If a record is marked as **'Urgent'**, the system automatically routes the call to the **Manager** for immediate human intervention.


---

# 👨‍💻 Bash Commands Used During Development

- ```python -m venv venv```: To isolate project dependencies.

- ```pip install```: To manage and install required Python packages.

- `python main.py`: To execute the core logic and test API integrations.

- `git commit -m "Update logic"`: To track changes and maintain version history.
