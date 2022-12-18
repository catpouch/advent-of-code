f = open("day15.txt", "r")

sensor_dists = set()
row_target = 2000000
covered = set()

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

for sensor, dist in sensor_dists:
    horiz_range = dist - abs(sensor[1] - row_target)
    for i in range(sensor[0] - horiz_range, sensor[0] + horiz_range): #why i don't need to add one to the second argument i have no clue
        covered.add(i)

print(len(covered))