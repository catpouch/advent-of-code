f = open("day10.txt", "r")


cycle = 0
x = 1
interest = [20, 60, 100, 140, 180, 220]
total = 0

def check_cycle():
    global cycle
    global interest
    global x
    global total
    if(cycle in interest):
        print(cycle, x, cycle * x)
        total += x * cycle

for line in f.readlines():
    if(line.startswith("noop")):
        cycle += 1
        check_cycle()
    else:
        cycle += 1
        check_cycle()
        cycle += 1
        check_cycle()
        x += int(line[5:].strip())

print(total)