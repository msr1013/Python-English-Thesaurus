import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word doesn't exist,please check it"


result = input("enter word: ")
result = result.lower()

print(translate(result))
