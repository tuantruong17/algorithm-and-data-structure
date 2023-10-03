n = int(input())
cards = [int(x) % 2 for x in input().split()]
stk = []
for card in cards:
    stk.append(card)
    if len(stk) >= 2 and stk[-1] == stk[-2]:
        stk.pop()
        stk.pop()
print(len(stk))