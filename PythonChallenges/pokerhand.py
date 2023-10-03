cards = input().strip().split()
d = {}
for card in cards:
    typ = card[0]
    if typ not in d:
        d[typ] = 0
    d[typ] += 1
print(d)
print(max(d.values()))