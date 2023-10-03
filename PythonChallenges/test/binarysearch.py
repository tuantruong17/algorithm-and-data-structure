def assrt(lst, target):
    a = find_better(lst, target)
    b = control(lst, target)
    print(a)
    print(b)
    print()
    return a == b

def control(lst, target):
    return len([x for x in lst if x > target])
    
def find_better(lst, target):
    if target >= lst[-1]:
        return 0
    hi = len(lst) - 1
    lo = 0
    mid = (lo + hi) // 2
    while lo != hi:
        print("lo, hi", lo, hi)
        if lst[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
        mid = (lo + hi) // 2
    return len(lst) - mid


# print(assrt([1,3,3,5,5,7,8,9,10], 5))
# print(assrt([1,3,5,7,8,9,10,11,12,13,14,15,16], 5))
# print(assrt([1,3,5,7,8,9,10], 8))
# print(assrt([0,1,1,1,1,1,1,10], 1))
print(assrt([1,3,5], 0))
print(assrt([1,3,5], 1))
print(assrt([1,3,5], 2))
print(assrt([1,3,5], 3))
print(assrt([1,3,5], 4))
print(assrt([1,3,5], 5))
print(assrt([1,3,5], 6))