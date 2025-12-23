data = []

with open('day3/input.txt', 'r') as file:
    for line in file:
        data.append(line)

def find_largest_index_in_range(start_idx, numbers, stop_idx):
    cur_lar_index = start_idx
    for n in range(start_idx, stop_idx - 1):
        if(int(numbers[cur_lar_index]) < int(numbers[n])):
            cur_lar_index = n
    return cur_lar_index

def find_index_with_value(n, list):
    indexes_to_remove = []
    for i in range(len(list)):
        if(list[i] == n):
            indexes_to_remove.append(i)
    return indexes_to_remove

def check_if_joltages_are_done(list):
    if len(list) == 12:
        #print("True")
        return True
    else:
        return False

def create_number_from_list(list_data):
    str_nr = ""
    for i in range(len(list_data)):
        str_nr += str(list_data[i])
    return int(str_nr)

def transform_list_to_ints(line_data):
    data = []
    for i in range(len(line_data)-1): #Sista index är \n
        data.append(int(line_data[i]))
    return data

def create_number_from_list(list_data):
    list_str = ''
    for i in range(len(list_data)):
        list_str += str(list_data[i])
    return int(list_str)

def get_list_length(list):
    return len(list)

def get_amount_of_shrink_needed(list):
    return get_list_length(list) - 12

def extract_part_of_list_based_on_shrink(shrink_size, list, start_index):
    if(check_if_sub_list_contains_same_number(list[start_index:shrink_size + start_index]) == False or len(list) - 1 == shrink_size + start_index):
        return list[start_index:shrink_size + start_index]
    else:
        additional_check = 1
        contains_non_same_number = False
        while contains_non_same_number == False:
            if(check_if_sub_list_contains_same_number(list[start_index:shrink_size + start_index + additional_check]) == False or len(list) - 1 == shrink_size + start_index + additional_check):
                print("Found a dal where it stops!: ", list[start_index:shrink_size + start_index + additional_check])
                return list[start_index:shrink_size + start_index + additional_check]
            else:
                if(additional_check > len(list)):
                    return list[start_index:shrink_size + start_index]
                additional_check += 1
                





def extract_index_with_largest_value(list):
    largest_index = 0
    for i in range(len(list)):
        if(list[largest_index] < list[i]):
            largest_index = i
    return largest_index

def extract_index_with_smallest_value(list):
    smallest_index = 0
    for i in range(len(list)):
        if(list[smallest_index] > list[i]):
            smallest_index = i
    return smallest_index 

def remove_low_number_parts(list, index, max_removals, operation_start_index):
    possible_removal = list[operation_start_index:operation_start_index + index]
    print("Possible removals : ", possible_removal, " Operation start index : ", operation_start_index, " end : ", operation_start_index + index)
    removal_amount = min(max_removals, len(possible_removal))
    for i in range(removal_amount):
        print("Removing : ", list[extract_index_with_smallest_value(possible_removal) + operation_start_index], " (index in list : ", extract_index_with_smallest_value(possible_removal) + operation_start_index, list)
        print("DEL : ", list[extract_index_with_smallest_value(possible_removal) + operation_start_index])
        del list[extract_index_with_smallest_value(possible_removal) + operation_start_index]
        del possible_removal[extract_index_with_smallest_value(possible_removal)]
    print("Updated list : ", list)
    return list

def check_if_sub_list_contains_same_number(sub_list):
    print("Sub list : ", sub_list)
    if(len(sub_list) == 0):
        return False
    number_to_check = sub_list[0]
    for i in range(len(sub_list)):
        if(sub_list[i] != number_to_check):
            return False
    return True

def remove_whole_sequence(list, operation_start_index, shrinking_needed, list_to_perform_on):
    for i in range(len(list_to_perform_on)):
        print("Len list : " , len(list))
        if(len(list) == 12):
            return list
        print("Current list : ", list, " Shrinking needed : ", shrinking_needed, " List size : ", len(list), " Operation index : ", operation_start_index, " Possible solution ? (Op index - i) : ", operation_start_index - i)
        print("DEL : ", list[operation_start_index])
     #   if(operation_start_index >= len(list)):
    #    del list[len(list) - 1]
        #else:
        del list[operation_start_index]
    return list

def check_if_index_is_last(list, operation_index):
    return len(list) - 1 == operation_index

def handle_1_index_case(list, operation_index):
    item_removed = False
    while item_removed == False:
        if check_if_index_is_last(list, operation_index):
            print("DEL : ", list[operation_index])
            del list[operation_index]
            return list
        next_index = operation_index + 1
        next_item_in_line = list[next_index]
        if next_item_in_line <= list[operation_index]:
            operation_index += 1
            continue
        else:
            print("DEL : ", list[operation_index])
            del list[operation_index]
            return list

total_score = 0
for line in data:
    list_data = transform_list_to_ints(line)
    list_size = get_list_length(list_data)
    while check_if_joltages_are_done(list_data) == False:
        print(list_data)
        shrinking_needed = get_amount_of_shrink_needed(list_data)
        operation_start_index = 0
        operation_peformed = False
        while(operation_peformed == False):
            list_to_perform_operation_on = extract_part_of_list_based_on_shrink(shrinking_needed, list_data, operation_start_index)
            print("List to perform on : ", list_to_perform_operation_on)
            if(len(list_to_perform_operation_on) == 1):
                print("ENTERING LIST DATA ", list_data)
                list_data = handle_1_index_case(list_data, operation_peformed)
                print(list_data)
                operation_peformed = True
                continue
            if(check_if_sub_list_contains_same_number(list_to_perform_operation_on)):
                list_data = remove_whole_sequence(list_data, operation_start_index, shrinking_needed, list_to_perform_operation_on) # Om list_to_perform_operation_on är 8, då ska vi kolla tills vi slutar "stega" neråt och det vänder och tar bort värdet i dalen.
                operation_peformed = True
                continue
            largest_index_in_sequence = extract_index_with_largest_value(list_to_perform_operation_on)
            print("Largest index : ", largest_index_in_sequence, " List to perform operation on : ", list_to_perform_operation_on, " Operation start index : ", operation_start_index)
            if(largest_index_in_sequence == 0):
                operation_start_index += 1
            else:
                list_data = remove_low_number_parts(list_data, largest_index_in_sequence, shrinking_needed, operation_start_index)
                print(list_data)
                operation_peformed = True
            print("Stuck at : " , list_data)
    print(list_data)
    print(create_number_from_list(list_data))
    total_score += create_number_from_list(list_data)
print(total_score)
