f = open("day6.txt", "r")

data = f.read()

# good luck!

answer = 14
for idx in range(len(data)):
    buffer = data[idx:idx+14]
    for i in range(len(buffer)):
        if buffer[i] in buffer[:i] + buffer[-(len(buffer)-i-1) if -(len(buffer)-i-1) != 0 else len(buffer):]:
            answer += 1
            break
    else:
        print(answer)
        break