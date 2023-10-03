a, b, h = [int(x) for x in input().split()]
result = 0
count = 0
while result < h:
    count += 1
    result += a
    if result >= h:
        break
    result -= b
print(count)