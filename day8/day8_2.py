import math

f = open("day8.txt", "r")

width = len(f.readline())

f.seek(0)

text = f.read()

def get_column(column):
    return [int(text[i]) for i in range(len(text)) if (i - column) % width == 0]

def get_row(row):
    return [int(text[i]) for i in range(len(text)) if row * width <= i <= row * width + width - 1 and text[i] != "\n"]

best_score = -1
for i in range(len(text)):
    if(text[i] == "\n"): continue
    row = get_row(math.floor(i / width))
    column = get_column(i % width)
    total = 0
    score = 1
    for j in reversed(row[:i % width]):
        total += 1
        if j >= int(text[i]):
            break
    score *= total
    total = 0
    for j in row[i % width + 1:]:
        total += 1
        if j >= int(text[i]):
            break
    score *= total
    total = 0
    for j in reversed(column[:math.floor(i / width)]):
        total += 1
        if j >= int(text[i]):
            break
    score *= total
    total = 0
    for j in column[math.floor(i / width) + 1:]:
        total += 1
        if j >= int(text[i]):
            break
    score *= total
    
    if score > best_score:
        best_score = score
    print(i / len(text) * 100)

print(best_score)