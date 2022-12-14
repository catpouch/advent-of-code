import json

f = open("day7.txt", "r")

total = 0
def bfs(current):
    global total
    for child in current.values():
        if(isinstance(child, int)) and child <= 100000:
            total += child
        elif(isinstance(child, dict)):
            bfs(child)

def parse_path(root, path):
    object = root
    for folder in path:
        object = object[folder]
    return object

def add_path(root, path, x):
    object = root
    for folder in path:
        object = object[folder]
        object["#"] += x

root = {}
path = []
add_path(root, path, 5)
for l in f.readlines()[2:]:
    line = l.strip()

    if(line.startswith("$ cd ")):
        if(line[5:] == ".."):
            path.pop()
        else:
            path.append(line[5:])
    elif(line == "$ ls"):
        continue
    elif(line.startswith("dir ")):
        parse_path(root, path)[line[4:]] = {"#": 0}
    else:
        add_path(root, path, int(line.split(" ")[0]))

bfs(root)
print(total)