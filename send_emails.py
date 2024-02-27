"""
Sends emails from Gmail account. The code should be run daily if the words change daily.
Follow the instructions from this link to enable/obtain your Google Account App password: 
https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
"""

# ----- BEGIN EDITING -----
day_num = 2 # Starts at 0
sender_email = 'maxg414244@gmail.com'
sender_password = 'icpw xqbe ofwc uwne'  # Input the App password here (NOT your Gmail password!)
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

df = pd.read_csv(f"day{day_num}.csv")

# Description of the Email
with open(f"description{day_num}.txt", "r") as file:
    desc = file.read()

# Iterate over each row in the DataFrame and send email
for index, row in df.iterrows():
    recipient_email = row['Email Address']
    body = f"{desc}\n\n Today's Word Assassins:\n\n {row['Sentence']}"
    send_email(sender_email, sender_password, recipient_email, email_subject, body)

print("Emails Sent!")