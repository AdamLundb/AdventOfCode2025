class splinter:
    def __init__(self, pos):
        self.beams_reached = 0
        self.loc = pos
    def has_reached(self):
        self.beams_reached += 1

class Level:
    def __init__(self, lvl, layout_string):
        self.level = lvl
        self.layout = layout_string
        self.indexes = []
        self.splitters = []
        self.timeLines_On_Level = 0
        self.find_Beam_Indexes_and_splitters()
    
    def find_Beam_Indexes_and_splitters(self):
        for i in range(len(self.layout)):
            if(self.layout[i] == "S" or self.layout[i].isnumeric()):
                self.indexes.append(i)
            if(self.layout[i] == "^"):
                self.splitters.append(splinter([i, self.level]))



def add_beams_from_previous_level(beam_indexes_from_last_level, line_of_last_level, line_of_current_level, Timelines):
    new_line = list(line_of_current_level)
    last_line = list(line_of_last_level)
    print(last_line)
    print(new_line)
    for i in range(len(beam_indexes_from_last_level)):
        if(new_line[beam_indexes_from_last_level[i]] != "^"):
            if(last_line[beam_indexes_from_last_level[i]] == 'S'):
                new_line[beam_indexes_from_last_level[i]] = '1'
            else:
                if(new_line[beam_indexes_from_last_level[i]].isnumeric()):
                   new_line[beam_indexes_from_last_level[i]] = str(int(last_line[beam_indexes_from_last_level[i]]) + int(new_line[beam_indexes_from_last_level[i]]))
                else:
                    new_line[beam_indexes_from_last_level[i]] = str(int(last_line[beam_indexes_from_last_level[i]]))
        if(new_line[beam_indexes_from_last_level[i]] == "^"):
            if(new_line[beam_indexes_from_last_level[i] + 1] == '.'):
                new_line[beam_indexes_from_last_level[i] + 1] = last_line[beam_indexes_from_last_level[i]]
            else:
                new_line[beam_indexes_from_last_level[i] + 1] = str(int(new_line[beam_indexes_from_last_level[i] + 1])+ int(last_line[beam_indexes_from_last_level[i]]))
            if(new_line[beam_indexes_from_last_level[i] - 1] == '.'):
                new_line[beam_indexes_from_last_level[i] - 1] = last_line[beam_indexes_from_last_level[i]]
            else:
                new_line[beam_indexes_from_last_level[i] - 1] = str(int(new_line[beam_indexes_from_last_level[i] - 1])+ int(last_line[beam_indexes_from_last_level[i]]))
            Timelines += 1
    return new_line, Timelines

def print_map(data):
    for i in range(len(data)):
        print(data[i].layout)

def sum_last_level(data):
    sum = 0
    for item in data[-1].layout:
        if item.isnumeric():
            sum += int(item)
    return sum

data = []

i = 0
timeLines = 1
with open('day7/input.txt', 'r') as file:
    for line in file:
        if(i == 0):
            data.append(Level(i, line[:-1]))
        else:
            splits = 0
            if(line[-1] == "\n"):
                updated_line, timeLines = add_beams_from_previous_level(data[i-1].indexes, data[i-1].layout, line[:-1], timeLines)
            else:
                updated_line, timeLines = add_beams_from_previous_level(data[i-1].indexes, data[i-1].layout, line, timeLines)
            new_level = Level(i, updated_line)
            new_level.timeLines_On_Level = timeLines
            data.append(new_level)
        i += 1

print_map(data)
print(sum_last_level(data))