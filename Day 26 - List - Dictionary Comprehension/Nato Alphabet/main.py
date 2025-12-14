import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {item.letter: item.code for item in df.itertuples() }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What's your name? ")
res  = [nato_dict[char] for char in name]

print(res)

