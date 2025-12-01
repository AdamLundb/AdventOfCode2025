def extract_number(string):
    number = ""
    for char in string:
        if char.isdigit():
            number += char
    return int(number)

def apply_correction(data):
    if data < 0:
        data = 100 + data
    if data >= 100:
        data = data - 100
    return data

def check_if_0(data):
    if data == 0:
        return True
    else:
        return False

def execute_instruction(instruction, operand, current_data):
    if instruction == "L":
        current_data -= operand
    else:
        current_data += operand
    current_data = apply_correction(current_data)
    return current_data

# FIXA så att R555 till exempel blir R55, dvs tar bara de två sista siffrorna
data = []

dial = 50
score = 0

with open('day1/test.txt', 'r') as file:
    for line in file:
        data.append(line)

for items in data:
    instruction = items[0]
    number = extract_number(items)
    dial = execute_instruction(instruction, number, dial)
    print("Dial is roated to :", number, "to point at", dial)
    if dial == 0:
        score += 1
print("Score:", score)