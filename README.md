# Word Assassins Game

- Rules can be found in description0.txt. 

Instructions to get the technical portion running:
- Get a CSV file of names and emails of participants, labeled names_emails.csv with headers (i.e. first line of the CSV) as "Full name,Email Address"
- Run generate_data.py first to generate ahead of time all of the target words for each person.
- Every day, to send the email, you should run python send_emails.py
    - Set up your Gmail account according to [this link](https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps) to automate emails. This is only done once
    - Every day that an email is sent there should be a new description file written (e.g. description1.txt, description2.txt, etc.).
    - I computed the scores manually and just used an external excel sheet, copying and pasting the leaderboard into the descriptions.