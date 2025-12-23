import re

data = []
ranges = []

with open('day2/input.txt', 'r') as file:
    for line in file:
        data.append(line)

for items in data:
    items_split = items.split(",")
    print(items_split)
    for i in range(len(items_split)):
        if(items_split[i] != "\n"):
            ranges.append(items_split[i])

def extract_havles(number):
    str_nr = str(number)
    if len(str_nr) % 2 == 1:
        return None
    else:
        half = int(len(str_nr)/2)
        return int(str_nr[:half]) , int(str_nr[half:])
    
def extract_number_of_sequences_to_check(number):
    str_nr = str(number)
    sequence_to_check = []
    for i in range(len(str_nr)):
        j = i + 1
        if len(str_nr) % j == 0 and  j <= len(str_nr)/2:
            sequence_to_check.append(j)
    return sequence_to_check

def create_number_to_check_sequence_with(sequence_length, whole_number_string):
    number_to_create = ""
    for i in range(sequence_length):
        #print("Adding number : ", whole_number_string[i])
        number_to_create += whole_number_string[i]
    return number_to_create


def check_if_any_sequences_are_repeated_in_number(sequences, number):
    str_nr = str(number)
    for sequence in sequences:
        #print(len(sequence), number)
        sequence_number = create_number_to_check_sequence_with(sequence, str_nr)
        length_of_sequence = len(str_nr) / len(str(sequence_number))
        #print("Sequence number : ", sequence_number, "number of times it has to exist : ", length_of_sequence)
        matches = re.findall(sequence_number, str_nr)
        if len(matches) == length_of_sequence:
            return True
    return False


def check_if_halves_are_equal(first_half, second_half):
    return first_half == second_half
        

def check_for_invalid_ids(start, end):
    i = start
    invalid_ids = []
    while i <= end:
        possible_sequences = extract_number_of_sequences_to_check(i)
        #print("Possible sequences : ", possible_sequences)
        if check_if_any_sequences_are_repeated_in_number(possible_sequences, i):
            invalid_ids.append(i)
            #print(possible_halves)
            print(i)
        i += 1
    print(invalid_ids)
    return invalid_ids


print(ranges)
sum_of_invalid_ids = 0
for item in ranges:
    ids = item.split("-")
    sum_of_invalid_ids += sum(check_for_invalid_ids(int(ids[0]), int(ids[1])))
print(sum_of_invalid_ids)