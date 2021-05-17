import json

data = json.load(open("data.json"))


def translate(word):
    return data[word]


result = input("enter word: ")

print(translate(result))
