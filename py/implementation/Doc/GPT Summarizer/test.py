import json5

with open("plaintext_summaries2.0/Ogury.txt") as file:
    data = file.read()
print(data)
newdata = json5.loads(data)
print(newdata)