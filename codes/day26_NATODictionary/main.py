import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in df.iterrows()}
print([dic[letter.upper()] for letter in input("Type a word\n")])
