f = open("day5.txt")

lines = f.readlines()

crates = [
    ["Q", "S", "W", "C", "Z", "V", "F", "T"],
    ["Q", "R", "B"],
    ["B", "Z", "T", "Q", "P", "M", "S"],
    ["D", "V", "F", "R", "Q", "H"],
    ["J", "G", "L", "D", "B", "S", "T", "P"],
    ["W", "R", "T", "Z"],
    ["H", "Q", "M", "N", "S", "F", "R", "J"],
    ["R", "N", "F", "H", "W"],
    ["J", "Z", "T", "Q", "P", "R", "B"]
]

def parse_instruction(line):
    a = line.split('from')
    a[0] = a[0][5:-1]
    b = a[1].split('to')
    b[0] = b[0][1:-1]
    b[1] = b[1][1:]
    a[1] = b[0]
    a.append(b[1])
    return [int(x) for x in a]

for line in [x.strip() for x in lines[10:]]:
    instruction = parse_instruction(line)
    moving = crates[instruction[1] - 1][-instruction[0]:]
    moving.reverse() # the only line differentiating this solution from the second one
    crates[instruction[2] - 1].extend(moving)
    crates[instruction[1] - 1] = crates[instruction[1] - 1][:-instruction[0]]

output = ""
for crate in crates:
    output += crate[-1]

print(output)