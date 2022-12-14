import math

f = open("day8.txt", "r")

width = len(f.readline())

f.seek(0)

text = f.read()

def get_column(column):
    return [int(text[i]) for i in range(len(text)) if (i - column) % width == 0]

def get_row(row):
    return [int(text[i]) for i in range(len(text)) if row * width <= i <= row * width + width - 1 and text[i] != "\n"]

total = 0
for i in range(len(text)):
    if(text[i] == "\n"): continue
    row = get_row(math.floor(i / width))
    column = get_column(i % width)
    visible = [True, True, True, True] # one boolean for each side, they get turned off if that side is not visible
    for j in row[:i % width]: # this gets just the right side
        if j >= int(text[i]): # if the current number is greater than or equal to the inspected tree, that side is not visible
            visible[0] = False
    for j in row[i % width + 1:]: # repeat above 3 more times with the other sides
        if j >= int(text[i]):
            visible[1] = False
    for j in column[:math.floor(i / width)]:
        if j >= int(text[i]):
            visible[2] = False
    for j in column[math.floor(i / width) + 1:]:
        if j >= int(text[i]):
            visible[3] = False
    if True in visible: # if the tree is visible from any angle
        total += 1
    print(i / len(text) * 100)

print(total)