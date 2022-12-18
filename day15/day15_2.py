f = open("testing.txt", "r")
# this solution is easily my worst yet
sensor_dists = set()
field_size = 4_000_000

def in_field(point):
    if point[0] < 0 or point[0] > field_size or point[1] < 0 or point[1] > field_size:
        return False
    else:
        return True

def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

for line in f.readlines():
    halves = line.strip().split(":")
    halves[0] = halves[0][10:]
    halves[1] = halves[1][22:]
    sensor = halves[0].split(", ")
    sensor = tuple(int(x[2:]) for x in sensor)
    beacon = halves[1].split(", ")
    beacon = tuple(int(x[2:]) for x in beacon)
    dist = manhattan(sensor, beacon)
    sensor_dists.add((sensor, dist))

def out_range(point):
    for sensor, dist in sensor_dists: # see line 36 for my comment on this
        if manhattan(point, sensor) <= dist:
            return False
    return True

def get_edges(point, dist):
    dist += 1
    output = set()
    for i in {(1, 1), (-1, 1), (1, -1), (-1, -1)}:
        for j in range(dist + 1): # excess iterations!!! don't care enough to fix this right now!!!
            p = (point[0] + i[0] * j, point[1] + i[1] * (dist - j))
            if in_field(p):
                output.add(p)
    return output

def scan():
    i = 1
    for sensor, dist in sensor_dists:
        for edge in get_edges(sensor, dist):
            if out_range(edge):
                return edge
        print(i / len(sensor_dists))
        i += 1

result = scan()
print(result[0] * 4_000_000 + result[1])