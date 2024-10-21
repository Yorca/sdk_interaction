

with open("uploaded_apks.txt", "r") as file:
    lines = file.readlines()
lines = [line.replace("\n", "") for line in lines]

test = []
for line in lines:
    if line in test:
        print(line)
    test.append(line)
