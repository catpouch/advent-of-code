import math

f = open("day9.txt", "r")

def sign(a): # get the sign of a number (-1 or 1)
    if a:
        return a // abs(a)
    else:
        return 0

def closest_target(head, tail): # this is the tough part
    target = tail
    dist = [head[0] - tail[0], head[1] - tail[1]] # distance in [x, y] format between the tail and head
    if(dist[0] == 0): # same column
        target[1] = head[1] - sign(dist[1]) # go just below/above the head
    elif(dist[1] == 0): # same row
        target[0] = head[0] - sign(dist[0]) # go just to the left/right of the head
    elif(not ((dist[0] in [-1, 1]) and (dist[1] in [-1, 1]))): # hehe! (tail is not diagonal to the head)
        target = [head[0] - (dist[0] - sign(dist[0])), head[1] - (dist[1] - sign(dist[1]))] # hoohoo! (put the tail next to the head as specified in the rules, don't even try figuring this one out)
    return target

h = [0, 0] # head
t = [0, 0] # tail
visited = set() # positions the tail has visited

for line in f.readlines():
    for i in range(int(line[2:])): # move in increments of 1 at a time, x number of times
        if line.startswith("L "):
            h[0] -= 1
        elif line.startswith("R "):
            h[0] += 1
        elif line.startswith("U "):
            h[1] += 1
        elif line.startswith("D "):
            h[1] -= 1
        t = closest_target(h, t) # calculating tail position
        visited.add(" ".join([str(x) for x in t])) # adding tails pos to the visited set

print(len(visited))