import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter a name: ").upper()
phonetic_code = {letter: data_dict[letter] for letter in name}
print(phonetic_code)
