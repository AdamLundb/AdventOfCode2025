class Operator:
    def __init__(self, indexes, operator, start):
        self.operator = operator
        self.amount_of_indexes = indexes
        self.start_index = start


data = []
operators = []
with open('day6/input.txt', 'r') as file:
    for line in file:
        #lines = line.split()
        if(line.find("*") == -1 or line.find("+") == -1):
            data.append(line[:-1])
        else:
            operators.append(line)

def create_operator_objects(string_list_operators, data):
    is_first_operator = True
    Operators_Data = []
    index_of_last_operator = 0
    print(string_list_operators)
    for i in range(len(string_list_operators[0])):
        #print("item : ", string_list_operators[0][i])
        if(string_list_operators[0][i] == "*" or string_list_operators[0][i] == "+"):
            if(is_first_operator == True):
                is_first_operator = False
                index_of_last_operator = i
                continue
            Operators_Data.append(Operator(i-index_of_last_operator - 1, string_list_operators[0][index_of_last_operator], index_of_last_operator))
            index_of_last_operator = i
    Operators_Data.append(Operator(len(data[0]) - index_of_last_operator, string_list_operators[0][index_of_last_operator], index_of_last_operator))
    return Operators_Data

def print_operators_data(op_data, list_data):
    for i in range(len(op_data)):
        print("Operator : ", op_data[i].operator, " Amount of indexes : ", op_data[i].amount_of_indexes, " Start index : ", op_data[i].start_index)
    print(len(list_data))
    print(list_data[0][op_data[0].start_index:op_data[1].start_index])

print(data)
print(operators)
op_data = create_operator_objects(operators, data)
print_operators_data(create_operator_objects(operators, data), data)

scores = []
for i in range(len(op_data)):
    score = 0
    for j in range(op_data[i].amount_of_indexes):
        number = ""
        for k in range(len(data)):
            number += data[k][op_data[i].start_index + j:op_data[i].start_index + 1 + j]
        if(j == 0):
            score = int(number)
        else:
            if(op_data[i].operator == "*"):
                score *= int(number)
            if(op_data[i].operator == "+"):
                score += int(number)
    scores.append(score) 
    print(scores)   
print(sum(scores))