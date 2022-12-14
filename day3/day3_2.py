f = open("day3.txt", "r")

l = f.readlines()

def priority(char):
    ascii_val = ord(char)
    if(ascii_val >= 65 and ascii_val <= 90): # magic numbers!!!!!
        return(ascii_val - 38)
    elif(ascii_val >= 97 and ascii_val <= 122):
        return(ascii_val - 96)
    else:
        raise SystemExit

total = 0
for i in range(len(l) // 3):
    a = l[i * 3]
    b = l[i * 3 + 1]
    c = l[i * 3 + 2]

    for char in a:
        if(char in b and char in c):
            total += priority(char)
            break

print(total)