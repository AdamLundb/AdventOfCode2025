data = []

with open('input.txt', 'r') as file:
    for line in file:
        data.append(line)

for items in data:
    print(items)