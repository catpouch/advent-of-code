import math

f = open("day12.txt", "r").read()

lines = [x.strip() for x in f.split("\n")]
width = len(lines[0])

def find_char(char):
    global lines
    global width
    index = "".join(lines).find(char)
    return (index % width, math.floor(index / width))

start = find_char("S")
end = find_char("E")
print(start, end)

def get_value(coord):
    if coord[0] >= width or coord[0] < 0 or coord[1] >= len(lines) or coord[1] < 0:
        return -1
    letter = lines[coord[1]][coord[0]]
    if(letter == "S"):
        return 1
    elif(letter == "E"):
        return 26
    return ord(letter) - 96

def get_pos(coord):
    return lines[coord[1]][coord[0]]

def get_dist(coord):
    return math.sqrt((end[0] - coord[0]) ** 2 + (end[1] - coord[1]) ** 2)

def get_neighbors(coord):
    n = [(coord[0] + 1, coord[1]), (coord[0] - 1, coord[1]), (coord[0], coord[1] + 1), (coord[0], coord[1] - 1)]
    output = []
    curr_val = get_value(coord)
    for c in n:
        val = get_value(c)
        if not (val > curr_val + 1 or val == -1):
            output.append(c)
    output.sort(key=get_dist)
    return(output)

def bfs(root):
    length = 0
    visited = set()
    current = [root]
    queued = set()
    while True:
        while len(current) != 0:
            target = current.pop()
            visited.add(target)
            if target == end:
                return length
            for neighbor in get_neighbors(target):
                if not neighbor in visited:
                    queued.add(neighbor)
        current = queued.copy()
        queued.clear()
        length += 1

print(bfs(start))