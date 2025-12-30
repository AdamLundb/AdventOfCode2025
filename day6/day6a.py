data = []
operators = []
with open('day6/input.txt', 'r') as file:
    for line in file:
        lines = line.split()
        if(lines[0].isnumeric()):
            data.append(lines)
        else:
            operators.append(lines)

print(data)
print(operators)
scores = []
for i in range(len(data[0])):
    score = 0
    for j in range(len(data)):
        if(j == 0):
            score = int(data[j][i])
        else:
            if(operators[0][i] == "*"):
                score *= int(data[j][i])
            elif(operators[0][i] == "+"):
                score += int(data[j][i])
            elif(operators[0][i] == "-"):
                score -= int(data[j][i])
            elif(operators[0][i] == "/"):
                score /= int(data[j][i])
    scores.append(score)
    print(score)
print(sum(scores))