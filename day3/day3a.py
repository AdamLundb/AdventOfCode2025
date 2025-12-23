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

total_score = 0
for line in data:
    line_len = len(line)
    first = find_largest_index_in_range(0, line, line_len - 1)
    second = find_largest_index_in_range(first + 1, line, line_len)
    score = int(str(line[first] + line[second]))
    total_score += score
print(total_score)