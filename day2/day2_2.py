f = open("day2.txt")

mappings = {
    "A": 0, #rock
    "B": 1, #paper
    "C": 2, #scissors
    "X": 0,
    "Y": 1,
    "Z": 2
}

score = 0
for line in f.readlines():
    score += mappings[line[2]] * 3
    if(line[2] == "X"):
        score += ((mappings[line[0]] - 1) % 3) + 1
    elif(line[2] == "Y"):
        score += mappings[line[0]] + 1
    else:
        score += ((mappings[line[0]] + 1) % 3) + 1

print(score)