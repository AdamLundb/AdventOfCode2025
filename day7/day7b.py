import copy

class Level:
    def __init__(self, lvl, layout_string):
        self.level = lvl
        self.layout = list(layout_string)
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

class TimeLine:
    def __init__(self, list_of_Levels, current_level):
        self.levels = list_of_Levels
        self.level = current_level

    def update_TimeLine(self, new_level):
        self.levels.append(new_level)
        self.level = self.level + 1

    def return_highest_level(self):
        return self.levels[self.level]
    def print_timeline(self):
        for i in range(len(self.levels)):
            print(self.levels[i].layout)

def add_beams_from_previous_level(beam_indexes_from_last_level, line_of_current_level, current_TimeLine, timelines):
    new_line = list(line_of_current_level)
    #print(len(timelines))
    #nt_TimeLine.print_timeline()
    for i in range(len(beam_indexes_from_last_level)):
        #print(new_line, beam_indexes_from_last_level[i], i)
        if(new_line[beam_indexes_from_last_level[i]] != "^"):
            new_line[beam_indexes_from_last_level[i]] = 'S'
            new_time_line = TimeLine(current_TimeLine.levels, current_TimeLine.level)
            new_time_line.update_TimeLine(Level(current_TimeLine.level + 1,new_line))
            timelines.append(new_time_line)
        if(new_line[beam_indexes_from_last_level[i]] == "^"):
            for j in range(2):
                if(j == 0):
                    left_line = copy.deepcopy(new_line)
                    left_line[beam_indexes_from_last_level[i] - 1] = 'S'
                    new_time_line = copy.deepcopy(TimeLine(current_TimeLine.levels, current_TimeLine.level))
                    new_time_line.update_TimeLine(Level(current_TimeLine.level + 1, left_line))
                    timelines.append(new_time_line)
                if(j == 1):
                    right_line = copy.deepcopy(new_line)
                    right_line[beam_indexes_from_last_level[i] + 1] = 'S'
                    new_time_line = copy.deepcopy(TimeLine(current_TimeLine.levels, current_TimeLine.level))
                    new_time_line.update_TimeLine(Level(current_TimeLine.level + 1, right_line))
                    timelines.append(new_time_line)
    #print(len(timelines))
    return timelines

def print_map(data):
    for i in range(len(data)):
        print(data[i].layout)

def check_if_timelines_cotains_level_of_previous(timelines, index_to_check):
    for i in range(len(timelines)):
        if(timelines[i].level == index_to_check):
            return True
    return False
def fetch_timeline_of_current_level(timelines, current_level):
    for i in range(len(timelines)):
        if(timelines[i].level == current_level):
            return i

data = []
Amount_of_lines = 0
with open('day7/test.txt', 'r') as file:
    for line in file:
        Amount_of_lines += 1
print(Amount_of_lines)


i = 0
trees = []
with open('day7/input.txt', 'r') as file:
    for line in file:
        print("Current Level : ", i)
        if(i == 0):
            start_line = list(line[:-1])
            first_level = Level(0, start_line)
            level_list = [first_level]
            trees.append(TimeLine(level_list, i))
        else:
            while check_if_timelines_cotains_level_of_previous(trees, i - 1) == True:
                time_line_to_handle = trees.pop(fetch_timeline_of_current_level(trees, i - 1))
                if(line[-1] == "\n"):
                    current_line = line[:-1]
                else:
                    current_line = line
                trees = add_beams_from_previous_level(time_line_to_handle.return_highest_level().indexes, current_line, time_line_to_handle, trees)
        i += 1
print(len(trees))
