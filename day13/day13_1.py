f = open("testing.txt", "r")

packets = []

def parse_list(string):
    if string.isdigit():
        return int(string)
    
    pass

for line in f.read().split("\n\n"):
    parts = line.split("\n")
    packet = (parse_list(parts[0]), parse_list(parts[1]))
    packets.append(packet)