import sys
n = int(input())
cost = []
result = sys.maxsize
for i in range(n):
    cost.append(int(input()))
dp = [None] * n
dp[0] = 0
for dx in range(1, n):
    print(dx)
    new_dp = [None] * n
    # fill forward
    for x in range(n):
        curr_cost = dp[x]   
        if curr_cost is not None:
            idx = x + dx
            if idx < n:
                new_dp[idx] = curr_cost + cost[idx]
    print(new_dp)
    # fill backward
    for x in range(n-1, -1, -1):
        if x - dx >= 0 and new_dp[x] is not None:
            new_dp[x - dx] = min(new_dp[x - dx] if new_dp[x - dx] else sys.maxsize, new_dp[x] + cost[x - dx])
    print(new_dp)
    result = min(result, new_dp[-1] if new_dp[-1] else sys.maxsize)
    dp = new_dp
print(result)