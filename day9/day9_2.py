import math

f = open("day9.txt", "r")

def sign(a):
    if a:
        return a // abs(a)
    else:
        return 0

def closest_target(head, tail):
    target = tail
    dist = [head[0] - tail[0], head[1] - tail[1]]
    if(dist[0] == 0):
        target[1] = head[1] - sign(dist[1])
    elif(dist[1] == 0):
        target[0] = head[0] - sign(dist[0])
    elif(not ((dist[0] in [-1, 1]) and (dist[1] in [-1, 1]))): # hehe!
        target = [head[0] - (dist[0] - sign(dist[0])), head[1] - (dist[1] - sign(dist[1]))]
    return target

h = [0, 0]
knots = [[0, 0] for i in range(8)]
t = [0, 0]
visited = set()

for line in f.readlines():
    for i in range(int(line[2:])):
        if line.startswith("L "):
            h[0] -= 1
        elif line.startswith("R "):
            h[0] += 1
        elif line.startswith("U "):
            h[1] += 1
        elif line.startswith("D "):
            h[1] -= 1
        knots[0] = closest_target(h, knots[0])
        for j in range(1, 8):
            knots[j] = closest_target(knots[j-1], knots[j])
        t = closest_target(knots[7], t)
        visited.add(" ".join([str(x) for x in t]))

print(len(visited))