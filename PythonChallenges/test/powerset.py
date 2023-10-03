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


print(powerset(4))