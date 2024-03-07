# Word Assassins Game

It’s a new day with targets of three
Better know their whereabouts!
Since three are coming for you with glee

Each one, a word,
As simple as which,
as divine as calyx
and some, as renounced as Taylor Swift

A friend asks for the remote—
but there is no TV.
The quiet man asks for a photo—
but he has no phone.
She reaches and asks about life—
you’ve never seen her before.

But hey! Maybe you can think.
Invoke a shield, then grab a drink
for you are not powerless in this game of many
A game of literary deceit and tyranny

Be careful, little sheep, as you are led to the slaughter,
But just in case, check if your word is daughter.

## Extra

Read the emails to have an understanding.

Instructions to get the technical portion running:

- Get a CSV file of names and emails of participants, labeled names_emails.csv with headers (i.e. first line of the CSV) as "Full name,Email Address"
- Run generate_data.py first to generate ahead of time all of the target words for each person.
- Every day, to send the email, you should run python send_emails.py
  - Set up your Gmail account according to [this link](https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps) to automate emails. This is only done once
  - Every day that an email is sent there should be a new description file written (e.g. description1.txt, description2.txt, etc.).
  - You can compute manually, or use spreadsheet magic.
