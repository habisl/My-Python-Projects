# Interactive python dictionary that retrives information from JSON
# Show the output if exists 
# Also able to give suggestion from close words
# If doesnt exist ask for new word
import json
from difflib import get_close_matches  

data = json.load(open("data.json"))


def translate(w):
    w = w.lower() 
    if w in data:
        return data[w]
    elif w.title() in data:  
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: # if word is more than 1 then provide suggestion
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
