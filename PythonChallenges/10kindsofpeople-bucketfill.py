r, c = map(int, input().split())

mat = []

for line in range(r):
    mat.append(list(input()))

componentId = 0
component = [[-1] * c for _ in range(r)]
for row in range(r):
    for col in range(c):
        if component[row][col] == -1:
            fringe = [(row, col)]
            while len(fringe) != 0:
                r1, c1 = fringe.pop()
                if component[r1][c1] == -1:
                    component[r1][c1] = componentId
                    if r1 != 0 and mat[r1][c1] == mat[r1 - 1][c1]:
                        fringe.append((r1 - 1, c1))
                    if r1 != r - 1 and mat[r1][c1] == mat[r1 + 1][c1]:
                        fringe.append((r1 + 1, c1))
                    if c1 != 0 and mat[r1][c1] == mat[r1][c1 - 1]:
                        fringe.append((r1, c1 - 1))
                    if c1 != c - 1 and mat[r1][c1] == mat[r1][c1 + 1]:
                        fringe.append((r1, c1 + 1))
            componentId += 1

num_cases = int(input())
for i in range(num_cases):
    r1, c1, r2, c2 = [int(x) - 1 for x in input().split()]
    if component[r1][c1] != component[r2][c2]:
        print("neither")
    elif mat[r1][c1] == "0":
        print("binary")
    else:
        print("decimal")