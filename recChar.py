# given a string, find the first repeating and non-repeating characters

given = "ABCBC"

# First Repeating
dict = {}

for letter in given:
    if letter in dict:
        print(letter)
        break
    else: dict[letter] = 1

# First Non-Repeating
dict = {}

for letter in given:
    dict[letter] = dict[letter] + 1 if letter in dict else 1

for i, (key, val) in enumerate(dict.items()):
    if val == 1:
        print(f"pos: {i}, key: {key}")
        break
    if i == len(dict) - 1 :
        print('None')