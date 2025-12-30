class Level:
    def __init__(self, lvl, layout_string):
        self.level = lvl
        self.layout = layout_string
        self.indexes = []
        self.splitters = []
        self.has_caused_split = 0
        self.find_Beam_Indexes_and_splitters()
    
    def find_Beam_Indexes_and_splitters(self):
        for i in range(len(self.layout)):
            if(self.layout[i] == "S"):
                self.indexes.append(i)
            if(self.layout[i] == "^"):
                self.splitters.append(i)



def add_beams_from_previous_level(beam_indexes_from_last_level, line_of_current_level):
    new_line = list(line_of_current_level)
    score = 0
    for i in range(len(beam_indexes_from_last_level)):
        #print(new_line, beam_indexes_from_last_level[i], i)
        if(new_line[beam_indexes_from_last_level[i]] != "^"):
            new_line[beam_indexes_from_last_level[i]] = 'S'
        if(new_line[beam_indexes_from_last_level[i]] == "^"):
            if(beam_indexes_from_last_level[i] == 0):
                new_line[beam_indexes_from_last_level[i] + 1] = 'S'
            elif(beam_indexes_from_last_level[i] == len(new_line) - 1):
                new_line[beam_indexes_from_last_level[i] - 1] = 'S'
            else:
                new_line[beam_indexes_from_last_level[i] + 1] = 'S'
                new_line[beam_indexes_from_last_level[i] - 1] = 'S'
            score += 1
    return new_line, score

def print_map(data):
    for i in range(len(data)):
        print(data[i].layout)

data = []

i = 0
with open('day7/input.txt', 'r') as file:
    for line in file:
        if(i == 0):
            data.append(Level(i, line[:-1]))
        else:
            splits = 0
            if(line[-1] == "\n"):
                updated_line, splits = add_beams_from_previous_level(data[i-1].indexes, line[:-1])
            else:
                updated_line, splits = add_beams_from_previous_level(data[i-1].indexes, line)
            new_level = Level(i, updated_line)
            new_level.has_caused_split = splits
            data.append(new_level)
        i += 1

print_map(data)

score = 0
for i in range(len(data)):
    score += data[i].has_caused_split
print(score)