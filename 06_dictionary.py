import json

phonebook = {
    "name": "Bé",
    "phone": "1212",
    "city": "Budapest",
    "name2": "Bé2"
}

data = [phonebook["name"], phonebook["phone"], phonebook["city"]]
# print(data)


phonebook2 = {
    "06307742828": {"name":"Bé", "city":"Budapest"},
    "06307742829": {"name":"Hirsch", "city":"Budapest"},
    "06307742823": {"name":"Who?", "city":"Debrecen"},
    "random-numbers": [1,3,9,6,15]
}

print(phonebook2["06307742829"]["name"])
print(phonebook2["random-numbers"][-1])

phonebook2["06307742828"]= {"what'sup": "nothing"}

f=open("dictionary.txt", "a")
# f.write("This is the dict")
f.write("ionary.txt!")
f.close()

filename = "phonebook.json"

with open(filename, "w") as f:
    json.dump(phonebook2,f)
    print("file dumped!")

# with open(filename, "w") as f:
#    f.write(str(phonebook2))

# with open(filename) as f:
#    data = f.read()
#    print(type(data))

with open(filename) as f:
    data = json.load(f)
    print (type(data))
