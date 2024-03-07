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

## Rules

Core Mechanic:

- If you get your target to say a word aloud, you get 1 point.
- If you say a word someone is trying to get you to say, you lose 1/3rd of a point.
- Let me know if you got someone inside of the group chat! Say "I got [X] with word [Y]"

Shielding Mechanic:

- If you think you know your assassin's word, look at them and say "Is your word for me [X]?" or something similar. Saying shield gives you a bonus point (in my heart)
- If you get it right, then you gain a third of a point and they lose a third of a point. They cannot kill you for the rest of the day.
- If you get it wrong, then you use up one of your 3 daily shields (do not carry over) and cannot use it on that person again for the rest of the day.
- If you use it on someone who is NOT your assassin you suffer EMBARRASSMENT and lose that shield.

Kamikaze:

- You can swap to KAMIKAZE instead of normal gameplay mode.
- People do not target you for the day, rather, you have to target ALL of them (makes spreadsheet easier)
- You get a list of EVERYONE playing and a word for them (here, words are shorter to make it easier.)
- You earn a percentage. If you kill x% of people, you get x% * 3.
- Shielding still works against you, but you only lose 1/10th of a point if it is successful. Similarly, they gain 1/10th of a point.
- For each person you kill, they each lose 1/10th of a point.

## Extra

Read the emails to have an understanding.

Instructions to get the technical portion running:

- Get a CSV file of names and emails of participants, labeled names_emails.csv with headers (i.e. first line of the CSV) as "Full name,Email Address"
- Run generate_data.py first to generate ahead of time all of the target words for each person.
- Every day, to send the email, you should run python send_emails.py
  - Set up your Gmail account according to [this link](https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps) to automate emails. This is only done once
  - Every day that an email is sent there should be a new description file written (e.g. description1.txt, description2.txt, etc.).
  - You can compute manually, or use spreadsheet magic.
