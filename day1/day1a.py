def extract_number(string):
    number = ""
    for char in string:
        if char.isdigit():
            number += char
    return int(number)

def take_last_two_digits(number):   
    str_nr = str(number)
    if len(str_nr) <= 1:
        return number
    return int(str_nr[-2:])

def apply_correction(data):
    multiplier = 1
    if data < 0:
        multiplier = -1
        data = take_last_two_digits(data) * multiplier
    else:
        data = take_last_two_digits(data)
    return data


def check_if_0(data):
    if data == 0:
        return True
    else:
        return False
    
def check_conversion(data):
    if data >= 100:
        data = data - 100
    if data < 0:
        data = 100 + data
    return data

def execute_instruction(instruction, operand, current_data):
    operand = apply_correction(operand)
    if instruction == "L":
        current_data -= operand
    else:
        current_data += operand
    current_data = check_conversion(current_data)
    return current_data

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
    #print("Dial is roated to :", number, "to point at", dial)
    if dial == 0:
        #print("Dial is roated to :", number, "to point at", dial)
        #print("SCORE")
        score += 1
print("Score:", score)