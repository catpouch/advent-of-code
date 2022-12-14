f = open("day10.txt", "r")


cycle = 0
x = 1
crt = []

def check_cycle():
    global cycle
    global crt
    global x
    print(cycle % 40, x)
    if((cycle % 40) in [x - 1, x, x + 1]):
        crt.append("#")
    else:
        crt.append(".")

for line in f.readlines():
    if(line.startswith("noop")):
        check_cycle()
        cycle += 1
    else:
        check_cycle()
        cycle += 1
        check_cycle()
        cycle += 1
        x += int(line[5:].strip())

print("\n".join([str(crt[x * 40:(x+1) * 40]) for x in range(len(crt) // 40)]))