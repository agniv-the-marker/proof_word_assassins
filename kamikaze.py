"""
Gives each person a word
"""

import pandas as pd
import numpy as np
import pickle
import os

from config import KAMIKAZE_LENGTH

threshold = KAMIKAZE_LENGTH # kamikaze threshold

with open("./word_banks/5000_words.txt", "r") as file:
    lines5000 = file.readlines()

words5000 = [word[:-1] for word in lines5000]

# only choose words that are at least 5 letters
# kamikaze are allowed other words, check kamikaze.py
kamikaze_words = [word for word in words5000 if len(word) > threshold]

# check if randomized list of words has been created
if not os.path.isfile('./k_data/permuted_kamikaze_words.pkl'):
    words = np.random.permutation(kamikaze_words)

    with open('./k_data/permuted_kamikaze_words.pkl', 'wb') as f:
        pickle.dump(words, f)

with open('./k_data/permuted_kamikaze_words.pkl', 'rb') as f:
    loaded_list = pickle.load(f)

#print(kamikaze_words)

targets_df = pd.read_csv("names_emails.csv")
targets_names = list(targets_df["Full name"])
target_length = len(targets_names)

kamikaze_df = pd.read_csv("kamikaze_names_emails.csv")
kami_names = list(kamikaze_df['Full name'])
kami_length = len(kami_names)

# permute the names differently every day
permutation = np.random.permutation(targets_names)

for j, target_name in enumerate(permutation):
    kamikaze_df[f'{target_name}_word'] = kamikaze_words[j*kami_length: (j+1)*kami_length]

kamikaze_df["Sentence"] = ["\n".join(["Targets:"] + [f"""{targets_names[i]}: {kamikaze_df[targets_names[i]+'_word'][j]}""" for i in range(target_length)]) for j in range(kami_length)]

kamikaze_df.to_csv(f'./k_data/kamikaze.csv', index=False)
