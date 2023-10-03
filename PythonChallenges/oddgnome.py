for _ in range(int(input())):
    nums = [int(x) for x in input().split()]
    start = nums[1]
    for i in range(2, nums[0]):
        if nums[i] != start + i - 1:
            print(i)
            break

