def shuffle(cards, typ):
    l = len(cards)
    result = []
    l1 = []
    l2 = []
    if typ == "out":
        l1 = cards[:(l+1)//2]
        l2 = cards[(l+1)//2:]
        
    if typ == "in":
        l2 = cards[:l//2]
        l = cards[l//2:]
    
    for i in range(min(len(l1), len(l2))):
        result.append(l1[i])
        result.append(l2[i])
    if len(l1) > len(l2):
        result.append(l1[-1])
    if len(l2) > len(l1):
        result.append(l2[-1])
    return result
        
num, typ = input().split()
n = int(num)
original_cards = list(range(n))
cards = shuffle(original_cards, typ)
print(cards)

count = 1
while cards != original_cards:
    count += 1
    cards = shuffle(cards, typ)
    print(cards)
print(count)