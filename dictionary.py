import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        result = data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        result = ask(get_close_matches(word, data.keys())[0])
    else:
        result = "Oops! That word doesnt exist! Please double-check it"
    return result

def ask(close_word):
    answer = input("Did you mean " + close_word + "? (y/n): ")
    if answer.lower() == "y":
        result = translate(close_word)
    else:
        result = "Well alrighty then, I couldnt find a close enough word!"
    return result

x = True
while x == True:
    word = input("Enter a word! Type 'esc' to exit: ")
    word = word.lower()
    if word == "esc":
        x = False
    else:
        print(translate(word))
