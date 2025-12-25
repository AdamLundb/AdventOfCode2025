data = []

with open('day4/input.txt', 'r') as file:
    for line in file:
        if(list(line)[-1] == '\n'):
            data.append(list(line)[:len(line) - 1])
        else:
            data.append(list(line))
# kom ihåg det är y, x

def check_if_coordinate_is_on_bounding_box(x, y, data):
    return x == 0 or x == len(data[0]) - 1 or y == 0 or y == len(data) - 1

def check_above(x, y, data):
    score = 0
    print( x, y)
    if(data[y-1][x-1] == '@' or data[y - 1][x - 1] == 'x'):
        temper = data[y-1]
        temp = data[y-1][x-1]
        score += 1
    if(data[y-1][x] == '@' or data[y - 1][x] == 'x'):
        temper = data[y-1]
        temp = data[y-1][x]
        score += 1
    if(data[y-1][x+1] == '@' or data[y - 1][x + 1] == 'x'):
        temper = data[y-1]
        temp = data[y-1][x+1]
        score += 1
    return score

def check_sides(x, y, data):
    score = 0
    if(data[y][x-1] == '@' or data[y][x - 1] == 'x'):
        temper = data[y]
        temp = data[y][x-1]
        score += 1
    if(data[y][x+1] == '@' or data[y][x + 1] == 'x'):
        temper = data[y]
        temp = data[y][x + 1]
        score += 1
    return score

def check_below(x, y, data):
    score = 0
    if(data[y+1][x-1] == '@' or data[y + 1][x - 1] == 'x'):
        temper = data[y+1]
        temp = data[y+1][x - 1]
        score += 1
    if(data[y+1][x] == '@' or data[y + 1][x] == 'x'):
        temper = data[y+1]
        temp = data[y+1][x]
        score += 1
    if(data[y+1][x+1] == '@' or data[y + 1][x + 1] == 'x'):
        temper = data[y+1]
        temp = data[y+1][x + 1]
        score += 1
    return score



def direct_comparision(x, y, data):
    score = 0
    score += check_above(x, y, data)
    score += check_sides(x, y, data)
    score += check_below(x, y, data)
    return score

def check_if_top_left_valid(x , y, data):
    if(x == 0 or y == 0):
        return 0
    if(data[y - 1][x - 1] == '@' or data[y-1][x - 1] == 'x'):
        temper = data[y-1]
        temp = data[y-1][x-1]
        return 1
    return 0

def check_if_above_valid(x, y, data):
    if(y == 0):
        return 0
    if(data[y - 1][x] == '@' or data[y - 1][x] == 'x'):
        temper = data[y-1]
        temp = data[y-1][x]
        return 1
    return 0

def check_if_top_right_valid(x, y, data):
    if(y == 0 or x == len(data[x]) - 1):
        return 0
    if(data[y - 1][x + 1] == '@' or data[y - 1][x + 1] == 'x'):
        temper = data[y-1]
        temp = data[y-1][x + 1]
        return 1
    return 0

def check_if_left_side_valid(x, y, data):
    if(x == 0):
        return 0
    if(data[y][x - 1] == '@' or data[y][x - 1] == 'x'):
        temper = data[y]
        temp = data[y][x - 1]
        return 1
    return 0


def check_if_right_side_valid(x, y, data):
    if (x == len(data[x]) - 1):
        return 0
    if(data[y][x + 1] == '@' or data[y][x + 1] == 'x'):
        temper = data[y]
        temp = data[y][x + 1]
        return 1
    return 0


def check_if_bottom_left_valid(x, y, data):
    if(x == 0 or y == len(data) - 1):
        return 0
    if(data[y + 1][x - 1] == '@' or data[y + 1][x - 1] == 'x'):
        temper = data[y+1]
        temp = data[y+1][x - 1]
        return 1
    return 0


def check_if_bottom_middle_valid(x, y, data):
    if(y == len(data) - 1):
        return 0
    if(data[y + 1][x] == '@' or data[y + 1][x] == 'x'):
        temper = data[y + 1]
        temp = data[y + 1][x]
        return 1
    return 0


def check_if_bottom_right_valid(x, y, data):
    if(y == len(data) - 1 or x == len(data[x]) - 1):
        return 0
    if(data[y + 1][x + 1] == '@' or data[y + 1][x+ 1] == 'x'):
        return 1
    return 0

def check_if_4_or_more_papers_around(score):
    return score < 4

def check_if_at_sign(x, y, data):
    if(data[y][x] == '@' or data[y][x] == 'x'):
        return True
    return False

y = 0
total_score = 0
while y <= len(data) - 1:
    x = 0
    print(x)
    while x <= len(data[0]) - 1:
        score = 0
        if(check_if_at_sign(x, y, data)):
            if(check_if_coordinate_is_on_bounding_box(x, y, data)):
                score += check_if_top_left_valid(x, y, data)
                score += check_if_top_right_valid(x, y, data)
                score += check_if_above_valid(x, y, data)
                score += check_if_left_side_valid(x, y, data) 
                score += check_if_right_side_valid(x, y, data)
                score += check_if_bottom_left_valid(x, y, data)
                score += check_if_bottom_middle_valid(x, y, data)
                score += check_if_bottom_right_valid(x, y, data)
            else:
                score += direct_comparision(x, y, data)
            if(check_if_4_or_more_papers_around(score)):
                #print("Reachable at : x:", x, " y: ",y," score :" ,score)
                total_score += 1
                #print(data[y])
                data[y][x] = '.'
                y = 0
                x = 0
                continue
        x += 1

    y += 1

for items in data:
    for item in items:
        print(item, " ", end = " ")
    print("\n")

print(total_score)
