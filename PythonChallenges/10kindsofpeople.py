# Credit to https://www.geeksforgeeks.org/find-the-number-of-islands-using-disjoint-set/

r, c = map(int, input().split())

mat = []

for line in range(r):
    mat.append(list(input()))


parent = list(range(r * c))
    
def find_group(hash_code):
    while parent[hash_code] != hash_code:
        hash_code = parent[hash_code]
    return hash_code

def union(hash_code1, hash_code2):
    parent[find_group(hash_code1)] = find_group(hash_code2)

def hash(row, col):
    return row * c + col

for row in range(r):
    for col in range(c):
        if row - 1 >= 0 and mat[row - 1][col] == mat[row][col]:
            union(hash(row, col), hash(row - 1, col))
        if col - 1 >= 0 and mat[row][col - 1] == mat[row][col]:
            union(hash(row, col), hash(row, col - 1))
        if col + 1 < c and mat[row][col + 1] == mat[row][col]:
            union(hash(row, col), hash(row, col + 1))
        if row + 1 < r and mat[row + 1][col] == mat[row][col]:
            union(hash(row, col), hash(row + 1, col))

num_cases = int(input())
for i in range(num_cases):
    r1, c1, r2, c2 = [int(x) - 1 for x in input().split()]
    if find_group(hash(r1, c1)) != find_group(hash(r2, c2)):
        print("neither")
    elif mat[r1][c1] == "0":
        print("binary")
    else:
        print("decimal")
