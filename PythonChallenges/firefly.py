n, h = [int(x) for x in input().split()]
l1 = []
l2 = []

def find_better(lst, target):
    if target >= lst[-1]:
        return 0
    hi = len(lst) - 1
    lo = 0
    mid = (lo + hi) // 2
    while lo != hi:
        if lst[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
        mid = (lo + hi) // 2
    return len(lst) - mid
# def find_better(lst, target):
#     return len([x for x in lst if x > target])

for i in range(n // 2):
    l1.append(int(input()))
    l2.append(int(input()))
s1 = sorted(l1)
s2 = sorted(l2)
result = 2 * n + 1
count = 0
for i in range(h):
    temp = 0
    temp += find_better(s1, i)
    temp += find_better(s2, h - i - 1)
    if temp == result:
        count += 1
    if temp < result:
        result = temp
        count = 1
    print(i, temp)
print("{0} {1}".format(result, count))
    
