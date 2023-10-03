n = int(input())
hi = 11
lo = 0
while n != 0:
    line = input()
    if line == "too low":
        lo = max(lo, n + 1)
    elif line == "too high":
        hi = min(hi, n - 1)
    else:
        if n < lo or n > hi:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        hi = 11
        lo = 0
    n = int(input())
