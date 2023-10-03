h, w, n, m = [int(x) for x in input().split()]
mat = []
ker = []
for i in range(h):
    mat.append([int(x) for x in input().split()])
for i in range(n):
    ker.append([int(x) for x in input().split()])
result = [[0] * (h - n + 1) for _ in range(w - m + 1)]
for i in range(h - n + 1):
    for j in range(w - m + 1):
        for x in range(n):
            for y in range(m):
                result[j][i] += mat[i + x][j + y] * ker[n - x - 1][m - y - 1]
for i in range(h - n + 1):
    print(" ".join([str(x[i]) for x in result]))
        