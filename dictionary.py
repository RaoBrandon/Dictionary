# We need to import the json library to use dictionary json file
import json
# get_close_matches allows us to predict what the user might have meant to
# input in the event that they make a spelling error
from difflib import get_close_matches

# Creates a new dictionary by opening the json file and attaching the
# dictionary to the new data variable
data = json.load(open("data.json"))


# Function that takes in a word and returns the definition of the word using
# The user input as a key
def translate(word):
    # If the word is in our json file then we can return the definition of it
    if word in data:
        result = data[word]
    # If the exact word is not in our json file we can rank similar words based
    # on how close they are using get_close_matches
    elif len(get_close_matches(word, data.keys())) > 0:
        # If the match is close enough, call the ask function to ask if thats
        # what they meant
        result = ask(get_close_matches(word, data.keys())[0])
    else:
        # We cannot find a word similar enough to the input
        result = "Oops! That word doesnt exist! Please double-check it"
    return result


# This function is called to ask whether a similar word is what the user meant
def ask(close_word):
    # Prompt for input on whether or not our guess is correct
    answer = input("Did you mean " + close_word + "? (y/n): ")
    if answer.lower() == "y":
        # If we are correct we can print the definition of the correct word
        result = translate(close_word)
    else:
        # We are not correct and couldnt find a similar enough word
        result = "Well alrighty then, I couldnt find a close enough word!"
    return result

# Loop that prompts user for words to find the definition of
x = True
while x:
    word = input("Enter a word! Type 'esc' to exit: ")
    word = word.lower()
    if word == "esc":
        x = False
    else:
        # Call the translate function to print its return value
        print(translate(word))
