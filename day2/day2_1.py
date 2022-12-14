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
    score += mappings[line[2]] + 1
    if(mappings[line[0]] == mappings[line[2]]):
        score += 3
    elif(mappings[line[0]] == (mappings[line[2]] - 1) % 3):
        score += 6

print(score)