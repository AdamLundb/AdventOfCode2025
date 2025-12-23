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

def calculate_extra_turns(number):
    str_nr = str(abs(number))
    if len(str_nr) > 2:
        print("ADDING SCORE : ", int(str_nr[:-2]))
        return int(str_nr[:-2])
    else:
        return 0

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



def fix_dial(dial):
    if dial == 100:
        return 0
    else:
        return dial
    
def check_if_scoring(data, score):
    if data >= 100:
        score += 1
        data = data - 100
    if data < 0:
        score += 1
        data = 100 + data
    return data, score

def check_if_passed_zero(inst, old_dial, move, score):
    if(inst == "L" and old_dial - move <= 0 and check_if_starting_position(old_dial) == False):
        print("PAssed, score : ", score + 1)
        return score + 1
    if(inst == "R" and old_dial + move >= 100 and check_if_starting_position(old_dial) == False):
        print("PAssed, score : ", score + 1)
        return score + 1
    return score

def check_if_starting_position(dial):
    if dial == 0:
        return True
    else:
        return False

def execute_instruction(instruction, operand, current_data, score):
    operand = apply_correction(operand)
    if instruction == "L":
        next_move = 100 - operand + current_data
    else:
        next_move = operand + current_data
    next_move = fix_dial(next_move)
    print("Dial is rotated : ", operand, " To point at : ", take_last_two_digits(next_move))
    score = check_if_passed_zero(instruction, current_data, operand, score)
    return take_last_two_digits(next_move), score

data = []

dial = 50
score = 0

with open('day1/test.txt', 'r') as file:
    for line in file:
        data.append(line)

for items in data:
    instruction = items[0]
    number = extract_number(items)
    score += calculate_extra_turns(number)
    #print("NUMBER: " ,number)



    if apply_correction(number) != 0:
        dial, score = execute_instruction(instruction, number, dial, score)
        #print("Dial is roated to :", number, "to point at", dial)
print("Score:", score)