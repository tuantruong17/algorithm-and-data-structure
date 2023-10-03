
t = int(input())
ugly = {}

def helper(current, colors):
    global count
    global best
    print(current, colors)
    if len(colors) == 0:
        count += 1
        if not best:
            best = " ".join(current)
    for color in colors:
        if len(current) != 0:
            old_color = current[-1]
            if old_color in ugly and color in ugly[old_color]:
                continue
        if color not in current:
            current.append(color)
            new_colors = colors.copy()
            new_colors.remove(color)
            helper(current, new_colors)
            current.pop()

for _ in range(t):
    count = 0
    best = None
    ugly = {}
    num_colors = int(input())
    colors = input().split()
    num_constraints = int(input())
    for i in range(num_constraints):
        c1, c2 = input().split()
        if c1 not in ugly:
            ugly[c1] = set([])
        ugly[c1].add(c2)
        if c2 not in ugly:
            ugly[c2] = set([])
        ugly[c2].add(c1)
    helper([], colors)
    print(count)
    print(best)

    



        