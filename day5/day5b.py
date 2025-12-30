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
    
def extract_fresh_reciepies(safe_ingrediants_set, range_to_check):
    start = range_to_check[0]
    end = range_to_check[1]
    for n in range(start, end + 1):
        safe_ingrediants_set.add(n)
    print("Updated ingrediant set : ", safe_ingrediants_set)
    return safe_ingrediants_set

def add_safe_ingrediant_range(safe_ranges):
    new_unions = []
    for range_start, range_end in safe_ranges:
        has_value_been_added = False
        for i, (range_start_union, range_end_union) in enumerate(new_unions):
            if range_start >= range_start_union and range_end <= range_end_union:
                has_value_been_added = True
                break
            if range_start < range_start_union and range_end >= range_start_union:
                new_unions[i][0] = range_start
                if range_end > range_end_union:
                    new_unions[i][1] = range_end
                has_value_been_added = True
                break
            if range_start <= range_end_union and range_end > range_end_union:
                new_unions[i][1] = range_end
                has_value_been_added = True
                break
        if(has_value_been_added == False):
            new_unions.append([range_start, range_end])
    return new_unions

def calculate_uniques(ranges):
    score = 0
    for range_start, range_end in ranges:
        score += range_end - range_start + 1
    return score

def reset_items():
    return 0, 0

def add_merged_safe_ranges(ranges):
    list_of_ranges = list(ranges)
    length_of_list = len(list_of_ranges)
    selected_object = 0
    has_changed_occured = False
    while selected_object < length_of_list:
        object_to_check_against = 0
        has_changed_occured = False
        print(list_of_ranges)
        selected_start_range = list_of_ranges[selected_object][0]
        selected_end_range = list_of_ranges[selected_object][1]
        while object_to_check_against < length_of_list:
            if(selected_object == object_to_check_against):
                object_to_check_against += 1
                continue
            check_against_start = list_of_ranges[object_to_check_against][0]
            check_against_end = list_of_ranges[object_to_check_against][1]
            if check_against_start > max(selected_end_range, selected_start_range) + 1:
                object_to_check_against += 1
                continue
            if check_against_end < min(selected_end_range, selected_start_range) - 1:
                object_to_check_against += 1 
                continue
            # båda
            if check_against_start <= selected_start_range and check_against_end >= selected_end_range:
                list_of_ranges[selected_object][0] = check_against_start
                list_of_ranges[selected_object][1] = check_against_end
                list_of_ranges.pop(object_to_check_against)
                has_changed_occured = True
                length_of_list = len(list_of_ranges)
                selected_object, object_to_check_against = reset_items()
                break
            # end range
            if check_against_end >= selected_end_range and check_against_start <= selected_end_range + 1:
                list_of_ranges[selected_object][0] = min(selected_start_range, check_against_start)
                list_of_ranges[selected_object][1] = max(selected_end_range, check_against_end)
                list_of_ranges.pop(object_to_check_against)
                has_changed_occured = True
                length_of_list = len(list_of_ranges)
                selected_object, object_to_check_against = reset_items()
                break
            #Start
            if check_against_start <= selected_start_range and check_against_end + 1 >= selected_start_range:
                list_of_ranges[selected_object][0] = min(selected_start_range, check_against_start)
                list_of_ranges[selected_object][1] = max(selected_end_range, check_against_end)
                list_of_ranges.pop(object_to_check_against)
                has_changed_occured = True
                length_of_list = len(list_of_ranges)
                selected_object, object_to_check_against = reset_items()
                break
            if check_against_start >= selected_start_range and check_against_end <= selected_end_range:
                list_of_ranges.pop(object_to_check_against)
                has_changed_occured = True
                length_of_list = len(list_of_ranges)
                selected_object, object_to_check_against = reset_items()
                break
            object_to_check_against += 1
        if(has_changed_occured == False):
            selected_object += 1
    return list_of_ranges


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
safe_ranges = set()
safe_ingrediants = set()
for item in range(len(items_to_check)):
    for numbers_to_check in range(len(list_of_ranges)):
        if(items_to_check[item] >= list_of_ranges[numbers_to_check][0] 
           and items_to_check[item] <= list_of_ranges[numbers_to_check][1]):
            print(list_of_ranges[numbers_to_check])
            safe_ranges.add((list_of_ranges[numbers_to_check][0], list_of_ranges[numbers_to_check][1]))
            #print("Number : ", items_to_check[item], " is between the range : ", list_of_ranges[numbers_to_check])
#print(safe_ranges)
#print(score)
#print(extract_fresh_reciepies(safe_ingrediants,(3,5)))

#for ranges in safe_ranges:
 #   safe_ingrediants = extract_fresh_reciepies(safe_ingrediants, ranges)

updated_ranges = add_safe_ingrediant_range(list_of_ranges)
print("New ranges : " , updated_ranges)
print("Score : ", calculate_uniques(updated_ranges))

new_list = add_merged_safe_ranges(list_of_ranges)
print("Merged list : ", new_list)
print("Score : ", calculate_uniques(new_list))

