n = int(input())
while n != 0:
    child = [[]] * n
    marble = [0] * n 
    hasParent = [False] * n
    for i in range(n):
        line = input()
        nums = [int(x) for x in line.split()]
        node, num_marble, num_child = nums[:3]
        marble[node - 1] = num_marble
        if num_child:
            child_lst = [x - 1 for x in nums[(-num_child):]]
            child[node - 1] = child_lst
            for item in child_lst:
                hasParent[item] = True

    def postorder_traversal(node, parent):
        res = 0
        for child_node in child[node]:
            res += postorder_traversal(child_node, node)
        if parent is not None:
            move = marble[node] - 1
            marble[parent] += move
            res += abs(move)
            marble[node] = 1
        return res

    root = hasParent.index(False)
    print(postorder_traversal(root, None))
    n = int(input())
