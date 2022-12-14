import math

f = open("day12.txt", "r").read()

lines = [x.strip() for x in f.split("\n")]
width = len(lines[0])

def find_char(char):
    global lines
    global width
    index = "".join(lines).find(char)
    return [index % width, math.floor(index / width)]

start = find_char("S")
end = find_char("E")

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
    n = [[coord[0] + 1, coord[1]], [coord[0] - 1, coord[1]], [coord[0], coord[1] + 1], [coord[0], coord[1] - 1]]
    output = []
    curr_val = get_value(coord)
    for c in n:
        val = get_value(c)
        if not (val > curr_val + 1 or val == -1):
            output.append(c)
    output.sort(key=get_dist)
    return(output)

shortest_path = 99999999

def dfs(coord, path, length):
    global shortest_path
    # print(path)
    # print(coord)
    if coord == end:
        if length < shortest_path:
            shortest_path = length
        print(shortest_path)
        return length
    if coord in path:
        return
    new_path = path.copy()
    new_path.append(coord)
    length += 1
    if length > shortest_path:
        return
    results = []
    for neighbor in get_neighbors(coord):
        result = dfs(neighbor, new_path, length)
        if result:
            results.append(result)
    if not results:
        return
    # print(results)
    return sorted(results)[0]
    # return results

print(dfs(start, [], 0))
# print(start, end)
# print(get_neighbors([0, 4]))
# print(get_neighbors([0, 2]))