n, w = [int(x) for x in input().split()]
weeks = []
for i in range(w+1):
    nums = [int(x) for x in input().split()]
    count = nums[0]
    choices = [(nums[i], nums[i + count]) for i in range(1, count + 1)]
    weeks.append(choices)
print(weeks)

dp = [None] * (n+1)
for price, sellable in weeks[0]:
    if sellable > n:
        dp[0] = (price * n, -price),
    else:
        dp[n - sellable] = (price * sellable, -price)
print(dp)
for week in range(1, w + 1):
    new_dp = [None] * (n + 1)
    for i in range(n+1):
        if dp[i]:
            cur_sale, first_price = dp[i]
            for price, sellable in weeks[week]:
                if sellable > i:
                    new_dp[0] = max(new_dp[0] if new_dp[0] else (-1, None), (cur_sale + price * i, first_price))
                else:
                    new_dp[i - sellable] = max(new_dp[i - sellable] if new_dp[i - sellable] else (-1, None), (cur_sale + price * sellable, first_price))
    print([(i, x[0]) for i, x in enumerate(new_dp) if x])
    dp = new_dp
best = 0
best_first_price = -1000
for item in dp:
    if not item:
        continue
    sale, first_price = item
    if sale > best:
        best = sale
        best_first_price = first_price
    elif sale == best and first_price > best_first_price:
        best_first_price = first_price
print(best)
print(-best_first_price)
