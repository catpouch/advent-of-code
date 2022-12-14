f = open("day3.txt", "r")

def priority(char):
    ascii_val = ord(char)
    if(ascii_val >= 65 and ascii_val <= 90): # magic numbers!!!!!
        return(ascii_val - 38)
    elif(ascii_val >= 97 and ascii_val <= 122):
        return(ascii_val - 96)
    else:
        raise SystemExit

total = 0
for line in f.readlines():
    common = set()
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    print(a, b)
    for char in a:
        if char in b:
            common.add(char)
    for char in common:
        total += priority(char)

print(total)