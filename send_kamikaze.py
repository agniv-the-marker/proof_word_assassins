from config import APP_PASSWORD, DAY_NUM

day_num = DAY_NUM # Starts at 0
sender_email = 'agnivsarkar@proofschool.org'
sender_password = APP_PASSWORD
email_subject = f'KAMIKAZE {day_num}'

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
df = pd.read_csv(f"./k_data/kamikaze.csv")

# Description of the Email

# if no email written for that day / i was lazy
desc = """Hey!

Kill.

Thanks,

Agniv Sarkar

"""

try:
    with open(f"./k_emails/kamikaze{day_num}.txt", "r") as file:
        desc = file.read()
except:
    pass

if desc !=  """Hey!\n\nKill.\n\nThanks,\n\nAgniv Sarkar\n\n""":
    desc += "\n\n Kill. As many as you can.\n\n"

# Iterate over each row in the DataFrame and send email
for index, row in df.iterrows():
    recipient_email = row['Email Address']
    body = f"{desc}\n\n Today's Word Assassins:\n\n {row['Sentence']}"
    send_email(sender_email, sender_password, recipient_email, email_subject, body)

print("Emails Sent!")