"""
Given a dataset of names and emails and a set number of days N, generates N csv files with random targets and (new) words.

Assuming the number of days the Word Assassins game runs is fixed in advance, this code should be run once.

Warning: This code might run into an issue if there are too many people, days, or targets per person, since we are sourcing from 5000 words and use unique words each day.
"""

from config import NUM_DAYS

# ----- BEGIN EDITING -----
num_targets_per_person = 3
english_enums = ["first", "second", "third", "fourth", "fifth"][:num_targets_per_person] # someone's gonna have to manually extend this so the length is equal to num_targets_per_person lol
num_days = NUM_DAYS
# ----- END EDITING -----

import pandas as pd
import numpy as np
import pickle
import os

with open("5000_words.txt", "r") as file:
    lines5000 = file.readlines()

words5000 = [word[:-1] for word in lines5000]

# only choose words that are at least 5 letters
# kamikaze are allowed other words, check kamikaze.py
long_words = [word for word in words5000 if len(word) > 4]

# check if randomized list of words has been created
if not os.path.isfile('./data/permuted_words.pkl'):
    words = np.random.permutation(long_words)

    with open('./data/permuted_words.pkl', 'wb') as f:
        pickle.dump(words, f)

with open('./data/permuted_words.pkl', 'rb') as f:
    loaded_list = pickle.load(f)

for day_num in range(num_days):
    df = pd.read_csv("names_emails.csv")
    names = list(df["Full name"])
    words_per_day = num_targets_per_person * len(names)

    words_so_far = day_num * words_per_day
    for i in range(num_days):
        df[f"target{i+1}word"] = long_words[words_so_far + i*len(names) : words_so_far + (i+1)*len(names)]

    # permute the names differently every day
    permutation = np.random.permutation(names)

    shifts = [1 + n * num_targets_per_person for n in range(num_targets_per_person)]

    for name in names:
        for i, shift in enumerate(shifts):
            df.loc[df["Full name"] == name, f"target{i+1}"] = permutation[(list(permutation).index(name) + shift) % len(names)]

    targets = [f"target{i+1}" for i in range(num_targets_per_person)]
    targets_words = [f"target{i+1}word" for i in range(num_targets_per_person)]

    df["Sentence"] = ["\n".join([f"Your {english_enums[i]} target is {df[targets[i]][x]} with the word \"{df[targets_words[i]][x]}\"" for i in range(num_targets_per_person)]) for x in range(len(df))]

    df.to_csv(f"./data/day{day_num}.csv", index=False)