f = open("day4.txt", "r")

total = 0
for line in f.readlines():
    pair = line.split(",")
    a = [int(x) for x in pair[0].split("-")] # First two values as a list of ints
    b = [int(x) for x in pair[1].split("-")] # Last two values as a list of ints
    if not ((a[0] < min(b) and a[1] < min(b)) or (a[0] > max(b) and a[1] > max(b))): # !(A is completely outside of B)
        total += 1

print(total)