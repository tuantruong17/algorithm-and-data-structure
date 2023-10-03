target = int(input())
child_to_parent = {}
line = ""
while line != "-1":
    line = input()
    nums = [int(x) for x in line.split()]
    for i in range(1, len(nums)):
        child_to_parent[nums[i]] = nums[0]
while target in child_to_parent:
    print(target, end=" ")
    target = child_to_parent[target]
print(target)
