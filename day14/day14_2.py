f = open("day14.txt", "r")

rock = set()
sand = set()
min_y = 0

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

combined = rock.copy()

max_y = sorted(rock, key=lambda x: x[1], reverse=True)[0][1] + 2

def add_coords(a, b):
    return (a[0]+b[0], a[1]+b[1])

def iterate(pos):
    offsets = [(0, 1), (-1, 1), (1, 1)]
    if pos[1] == max_y - 1:
        return -1
    for offset in offsets:
        new = add_coords(pos, offset)
        if not new in combined:
            return new
    return -1

def sim_sand():
    global sand
    while not (500, 0) in sand:
        sand_pos = (500, 0)
        while True:
            new_pos = iterate(sand_pos)
            if new_pos == -1:
                sand.add(sand_pos)
                combined.add(sand_pos)
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