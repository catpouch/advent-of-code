f = open("day1.txt", "r")

greatest = [0, 0, 0]
total_sum = 0
for line in f.readlines():
    if(line == "\n"):
        greatest.append(total_sum)
        greatest.sort()
        greatest.pop(0)
        total_sum = 0
    else:
        total_sum += int(line)

print(greatest)
print(sum(greatest))