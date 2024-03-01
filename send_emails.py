"""
Sends emails from Gmail account. The code should be run daily if the words change daily.
Follow the instructions from this link to enable/obtain your Google Account App password: 
https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
"""

from os import environ
from config import APP_PASSWORD

# ----- BEGIN EDITING -----
day_num = 2 # Starts at 0
sender_email = 'agnivsarkar@proofschool.org'
sender_password = APP_PASSWORD
email_subject = f'Word Assassins Day {day_num}'
# ----- END EDITING -----

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    
    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))
    
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Use the appropriate SMTP server
    session.starttls()  # Enable encryption
    session.login(sender_email, sender_password)  # Login with your Gmail account
    text = message.as_string()
    session.sendmail(sender_email, recipient_email, text)
    session.quit()

num = day_num % 5
df = pd.read_csv(f"day{num}.csv")

# Description of the Email

# if no email written for that day / i was lazy
desc = """Hey Everyone!

Time for another good round! Happy hunting!

From,

Agniv Sarkar

"""

try:
    with open(f"description{day_num-1}.txt", "r") as file:
        desc = file.read()
except:
    pass

# Iterate over each row in the DataFrame and send email
for index, row in df.iterrows():
    recipient_email = row['Email Address']
    body = f"{desc}\n\n Today's Word Assassins:\n\n {row['Sentence']}"
    send_email(sender_email, sender_password, recipient_email, email_subject, body)

print("Emails Sent!")