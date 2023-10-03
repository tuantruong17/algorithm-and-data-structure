import math
n = int(input())
best_slope = 1
pts = [int(x) for x in input().split()]
top = max(enumerate(pts), key=lambda x: x[1])
for i in range(0, top[0]):
    pt = pts[i]
    slope = (top[1] - pt) / (top[0] - i)
    best_slope = min(best_slope, slope)
distance = (top[1] - (pts[0] + 4)) / best_slope
print(max(math.floor(distance - top[0] + 1), 0))