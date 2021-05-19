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
            return data[get_close_matches(w, data.keys())[0]]
        elif inp == 'n':
            return 'The word doesnt exist,please double check it!'

        else:
            return "We donot understand your entry"

    else:
        return "Sorry no matches,word doesnt exist please double check"


result = input("enter word: ")
result = result.lower()

output = translate(result)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
