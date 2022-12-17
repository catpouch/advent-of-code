f = open("day15.txt", "r")

sensor_dists = set()

for line in f.readlines():
    halves = line.strip().split(":")
    halves[0] = halves[0][10:]
    halves[1] = halves[1][22:]
    sensor = halves[0].split(", ")
    sensor = tuple(int(x[2:]) for x in sensor)
    beacon = halves[1].split(", ")
    beacon = tuple(int(x[2:]) for x in beacon)
    print(sensor, beacon)