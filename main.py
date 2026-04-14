import os
import time
import requests
from pyairtable import Table
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Saari credentials (Same as Phase 3)
AIRTABLE_TOKEN = os.getenv('AIRTABLE_API_KEY')
BASE_ID = os.getenv('AIRTABLE_BASE_ID')
TABLE_NAME = os.getenv('TABLE_NAME')
OPENROUTER_KEY = os.getenv('OPENROUTER_API_KEY')
TWILIO_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('TWILIO_PHONE_NUMBER')
MY_NUMBER = os.getenv('MY_PERSONAL_NUMBER')

def run_automated_agent():
    print("--- 🤖 Phase 4: Automated Agent is Running ---")
    while True: # Ye infinite loop hai
        try:
            table = Table(AIRTABLE_TOKEN, BASE_ID, TABLE_NAME)
            records = table.all()
            
            found_pending = False
            for record in records:
                fields = record.get('fields', {})
                if fields.get('Status') == "Pending":
                    found_pending = True
                    # ... (Yahan wahi saara message bhejne ka code aayega) ...
                    print(f"Processed {fields.get('Name')}")
            
            if not found_pending:
                print("No pending records found. Sleeping for 1 hour...")
            
            # 1 Ghante (3600 seconds) ke liye wait karega
            time.sleep(3600) 
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60) # Error aane par 1 min wait karke retry karega