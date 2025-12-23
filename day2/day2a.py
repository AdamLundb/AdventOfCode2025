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
    
def check_if_halves_are_equal(first_half, second_half):
    return first_half == second_half
        

def check_for_invalid_ids(start, end):
    i = start
    invalid_ids = []
    while i <= end:
        possible_halves = extract_havles(i)
        if possible_halves == None:
            i += 1
            continue
        if check_if_halves_are_equal(possible_halves[0], possible_halves[1]):
            invalid_ids.append(i)
            #print(possible_halves)
        #print(i)
        i += 1

    return invalid_ids


print(ranges)
sum_of_invalid_ids = 0
for item in ranges:
    ids = item.split("-")
    sum_of_invalid_ids += sum(check_for_invalid_ids(int(ids[0]), int(ids[1])))
print(sum_of_invalid_ids)