import pandas as pd
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Load recipients
df = pd.read_csv('recipients.csv')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for index, row in df.iterrows():
        msg = EmailMessage()
        msg['Subject'] = 'Join CodeSakhi: a teeny tiny reminder!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = row['email']
        msg.set_content(f"""
        Hey girls,
        We are finallyyy close to launching the community and excited wouldnt cover how we are feeling rn. 
        To get things started ASAP, pleasee join the whatsapp community given below: 
        https://chat.whatsapp.com/FdprFFhcHKk0sUHEA6r4Zw

        This is where you’ll connect with mentors and other brilliant girls, and get all the latest updates.
        We have some AWESOMEEE things planned for you, let's work together and make them come true!!
                        
        Stay in the loop with us:
        LinkedIn: @CodeSakhi
        Instagram: https://www.instagram.com/codesakhi/

        See you inside!
                        
        P.S. if you have already joined the community (ignore us lol)
        
        Love,
        Anjana
        Code Sakhi
        """)

        try:
            smtp.send_message(msg)
            print(f"Sent to {row['email']}")
        except Exception as e:
            print(f"Failed to send to {row['email']}: {e}")

