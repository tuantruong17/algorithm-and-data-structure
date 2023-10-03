
def gcd(x, y): # only for x, y non negative
    if x % y == 0:
        return y
    if y % x == 0:
        return x
    if x > y:
        return gcd(x % y, y)
    # x is always less than y here
    return gcd(y % x, x)

num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    wheels = []
    for i in range(n):
        wheel = [int(x) for x in input().split(" ")]
        spin = None
        if i == 0:
            spin = [1, 1, True]
        wheel.append(spin)
        wheels.append(wheel)
    graph = [[] for _ in range(n)]
    bag = set(range(1, n))
    last_visited = [0]
    new_visited = [None]
    while len(new_visited) != 0:
        new_visited = []
        for i1 in last_visited:
            bag_del = []
            for i2 in bag:
                x1, y1, r1, s1 = wheels[i1]
                x2, y2, r2, s2 = wheels[i2]
                if round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5) == r1 + r2:
                    graph[i1].append(i2)
                    bag_del.append(i2)
                    new_visited.append(i2)

                    top, bot, sign = s1
                    d = gcd(top * r1, bot * r2)
                    wheels[i2][3] = [top * r1 // d, bot * r2 // d, not sign]
            for item in bag_del:
                bag.remove(item)
        last_visited = new_visited

for wheel in wheels:
    if wheel[3] == None:
        print("not moving")
        continue
    top, bot, sign = wheel[3]
    print("{0}{1} {2}".format(abs(top), "/" + str(bot) if bot != 1 else "", "clockwise" if sign else "counterclockwise"))

