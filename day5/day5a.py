data = []

with open('day5/input.txt', 'r') as file:
    for line in file:
        data.append(line)

def strip_newline(item):
    possible_newline_location = item.find("\n")
    if(possible_newline_location == -1):
        return int(item)
    else:
        return int(item[:possible_newline_location])

list_of_ranges = []
items_to_check = []
for items in data:
    if(len(items.split("-")) > 1):
        ranges = items.split("-")
        ranges = [strip_newline(ranges[0]), strip_newline(ranges[1])]
        list_of_ranges.append(ranges)
    elif(items == '\n'):
        continue
    else:
        items_to_check.append(strip_newline(items))
print(items_to_check)
print(list_of_ranges)

score = 0
for item in range(len(items_to_check)):
    for numbers_to_check in range(len(list_of_ranges)):
        if(items_to_check[item] >= list_of_ranges[numbers_to_check][0] 
           and items_to_check[item] <= list_of_ranges[numbers_to_check][1]):
            score += 1
            print("Number : ", items_to_check[item], " is between the range : ", list_of_ranges[numbers_to_check])
            break
print(score)
