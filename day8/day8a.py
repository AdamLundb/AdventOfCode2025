import math

class JunctionBox:
    def __init__(self, x_cord, y_cord, z_cord, new_id):
        self.id = new_id
        self.x = int(x_cord)
        self.y = int(y_cord)
        if z_cord[-1] == "\n":
            self.z = int(z_cord[:-1])
        else:
            self.z = int(z_cord)
    def give_coordinates(self):
        return [self.x, self.y, self.z]

class Connections:
    def __init__(self, box1, box2, straight_line_distance):
        self.connections = [box1, box2]
        self.dist = straight_line_distance
    def add_box_to_connection(self, new_box):
        self.connections.append(new_box)
    def return_unique_box(self, check_box1, check_box2):
        unique_boxes = []
        if(check_box1 not in self.connections and check_box2 not in self.connections):
            return self.connections
        if(check_box1 != self.connections[0]):
            unique_boxes.append(self.connections[0])
        if(check_box1 != self.connections[1]):
            unique_boxes.append(self.connections[1])
        if(check_box2 != self.connections[0]):
            unique_boxes.append(self.connections[0])
        if(check_box2 != self.connections[1]):
            unique_boxes.append(self.connections[1])
        return unique_boxes
    def print_connection(self):
        print(f"Box with id : {self.connections[0].id} and coordinates : {self.connections[0].give_coordinates()} and Box with id : {self.connections[1].id} and coordinates {self.connections[1].give_coordinates()} has a distance of : {self.dist}")


def find_straight_line_distance_between_junction_boxes(box1, box2):
    distance = math.sqrt(pow(box2.x - box1.x, 2) + pow(box2.y - box1.y, 2) + pow(box2.z - box1.z, 2))
    return distance

def find_connections(junction_box_list):
    possible_connections = []
    for i in range(len(junction_box_list)):
        for j in range(i+1 , len(junction_box_list)):
            if(i + 1 == len(junction_box_list)):
                continue
            straight_line_dist = find_straight_line_distance_between_junction_boxes(junction_box_list[i], junction_box_list[j])
            new_connection = Connections(junction_box_list[i], junction_box_list[j], straight_line_dist)
            possible_connections.append(new_connection)
    return possible_connections

def add_connection_at_right_spot(connection_list, connection, list_size):
    if(len(connection_list) == 0):
        connection_list.append(connection)
        return connection_list
    valid_pos = -1
    for i in range(len(connection_list)):
        if(connection.dist < connection_list[i].dist):
            valid_pos = i
            break
    if(valid_pos != -1):
        connection_list.insert(valid_pos, connection)
    if(len(connection_list) < list_size and valid_pos == -1):
        connection_list.append(connection)
    if(len(connection_list) > list_size):
        connection_list.pop(-1)
    return connection_list

def find_x_smallest_connections(connection_list):
    smallest_connection_list = []
    for i in range(len(connection_list)):
        smallest_connection_list = add_connection_at_right_spot(smallest_connection_list, connection_list[i], 10)
    return smallest_connection_list

#tänk över detta
def find_possible_larger_connections(connection_list):
    inspected_boxes = []
    different_connections = []
    for i in range(len(connection_list)):
        box1 = connection_list[i].connections[0]
        box2 = connection_list[i].connections[1]
        connection = [box1.id, box2.id]
        if(box1 and box2 not in inspected_boxes):
            inspected_boxes.append(box1)
            inspected_boxes.append(box2)
            for j in range(len(connection_list)):
                if(len(connection_list[j].return_unique_box(box1, box2)) == 1):
                    connection.append(connection_list[j].return_unique_box(box1, box2)[0].id)
                    inspected_boxes.append(connection_list[j].return_unique_box(box1, box2)[0])
            different_connections.append(connection)
    return different_connections

def find_largest_connections(largest_connections):
    for i in range(len(largest_connections)):
        swapped = False
        for j in range(0, len(largest_connections[i]) - i - 1):
            if len(largest_connections[j]) > len(largest_connections[j + 1]):
                largest_connections[j], largest_connections[j + 1] = largest_connections[j + 1], largest_connections[j]
                swapped = True
        if (swapped == False):
            break
    return [len(largest_connections[-1]), len(largest_connections[-2]), len(largest_connections[-3])]
junction_boxes = []

with open('day8/test.txt', 'r') as file:
    n = 0
    for line in file:
        coords = line.split(",")
        junction_boxes.append(JunctionBox(coords[0], coords[1], coords[2], n))
        n = n + 1

possible_connections = find_connections(junction_boxes)
for connection in possible_connections:
    connection.print_connection()
smallest_connections = find_x_smallest_connections(possible_connections)
print("Smallest connections : ")
for connection in smallest_connections:
    connection.print_connection()
#the_connections = find_possible_larger_connections(smallest_connections)
#print(the_connections)
#largest_connections = find_largest_connections(the_connections)
#print("Connections : ", largest_connections[0] * largest_connections[1] * largest_connections[2])


