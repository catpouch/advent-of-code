import ast

f = open("day13.txt", "r")
text = f.read()
text += "\n[[2]]\n[[6]]"

packets = []
for line in text.split("\n"):
    if not line:
        continue
    packet = ast.literal_eval(line)
    packets.append(packet)

def dfs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return
    elif isinstance(left, list) and isinstance(right, list):
        for i, j in zip(left, right):
            r = dfs(i, j)
            if r != None:
                return r
        if len(left) < len(right):
            return True
        if len(right) < len(left):
            return False
        else:
            return
    else:
        if isinstance(left, int):
            return dfs([left], right)
        else:
            return dfs(left, [right])

for _ in range(len(packets)):
    for index in range(len(packets) - 1):
        if not dfs(packets[index], packets[index + 1]):
            a = packets.pop(index)
            packets.insert(index + 1, a)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))