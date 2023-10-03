def powerset(n):
    ans = []
    helper([], 0, n, ans)
    return ans

def helper(current, index, n, ans):
    if index == n:
        ans.append(current)
        return
    helper(current + [index], index + 1, n , ans)
    helper(current + [], index + 1, n , ans)
    
n = int(input())
bags = []
for i in range(n):
    nums = [int(x) for x in input().split()]
    types = nums[0]
    bag = {}
    for j in range(types):
        index = 2 * j + 1
        candy_type = nums[index]
        count = nums[index + 1]
        bag[candy_type] = count
    bags.append(bag)

if all([len(bag) == 1 for bag in bags]):
    d = {}
    for bag in bags:
        for item in bag: # there should always be one item
            if item not in d:
                d[item] = 0
            d[item] += bag[item]
    for key in d:
        if key < 0 and -key in d:
            d[-key] = max(d[-key], d[key])
            d[key] = 0
    print(sum(d.values()))
elif n <= 15:
    result = 0
    for choice in powerset(n):
        d = {}
        for index in choice:
            bag = bags[index]
            for item in bag:
                if abs(item) not in d:
                    d[abs(item)] = 0
                if item > 0:
                    d[item] += bag[item]
                else:
                    d[-item] -= bag[item]
        candies = sum([abs(x) for x in d.values()])
        if candies > result:
            result = candies
    print(result)
    


