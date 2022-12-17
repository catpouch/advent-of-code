f = open("day14.txt", "r")

rock = set()
sand = set()

def fill_line(a, b):
    if a[0] == b[0]:
        for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
            rock.add((a[0], i))
    elif a[1] == b[1]:
        for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            rock.add((i, a[1]))

for line in f.readlines():
    points = line.strip().split(" -> ")
    for i in range(len(points) - 1):
        raw_coords = points[i].split(",")
        a = (int(raw_coords[0]), int(raw_coords[1]))
        raw_coords = points[i + 1].split(",") # mutable data because i can't think of good variable names!!!
        b = (int(raw_coords[0]), int(raw_coords[1]))
        fill_line(a, b)

def add_coords(a, b):
    return (a[0]+b[0], a[1]+b[1])

def iterate(pos):
    combined = rock.union(sand)
    filtered = list(filter(lambda p: p[0] == pos[0] and p[1] >= pos[1], combined))
    if len(filtered) == 0:
        return -1
    else:
        nearest_floor = sorted(filtered, key=lambda x: x[1])[0]
        nearest_floor = (nearest_floor[0], nearest_floor[1] - 1)
    offsets = [(-1, 1), (1, 1)]
    if nearest_floor != pos:
        return nearest_floor
    for offset in offsets:
        new = add_coords(pos, offset)
        if not new in combined:
            return new
    return -2

def sim_sand():
    global sand
    finished = False
    while not finished:
        sand_pos = (500, 0)
        while True:
            new_pos = iterate(sand_pos)
            if new_pos == -1:
                finished = True
                break
            if new_pos == -2:
                sand.add(sand_pos)
                break
            sand_pos = new_pos

def print_field():
    combined = rock.union(sand)
    sorted_x = sorted(combined)
    sorted_y = sorted(combined, key=lambda x: x[1])
    limits_x = (sorted_x[0][0], sorted_x[-1][0] + 1)
    limits_y = (sorted_y[0][1], sorted_y[-1][1] + 1)
    for i in range(limits_y[0], limits_y[1]):
        print(str(i).zfill(len(str(limits_y[1]))), end="")
        for j in range(limits_x[0], limits_x[1]):
            if (j, i) in rock:
                print("#", end="")
            elif (j, i) in sand:
                print("\033[96mo\033[0m", end="")
            else:
                print(".", end="")
        print("")

sim_sand()
print_field()
print(len(sand))