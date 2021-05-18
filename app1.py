import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        inp = input("Did you mean %s instead? Enter y if Yes or n if No :" %
                    get_close_matches(w, data.keys())[0])
        if inp == 'y':
            print(data[get_close_matches(w, data.keys())[0]])

        else:
            return "The word doesn't exist,please check it"


result = input("enter word: ")
result = result.lower()

print(translate(result))
