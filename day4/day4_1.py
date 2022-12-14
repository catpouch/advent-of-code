f = open("day4.txt", "r")

total = 0
for line in f.readlines():
    pair = line.split(",")
    a = [int(x) for x in pair[0].split("-")] # First two values as a list of ints
    b = [int(x) for x in pair[1].split("-")] # Last two values as a list of ints
    if((a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1])): # A encapsulates B, or the other way around
        total += 1

print(total)