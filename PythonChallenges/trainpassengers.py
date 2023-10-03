c, n = [int(x) for x in input().split()]
current = 0

def helper(n):
    global current
    for i in range(n):
        left, entered, stayed = [int(x) for x in input().split()]
        current -= left
        if current < 0:
            print("impossible")
            return
        current += entered
        if current > c:
            print("impossible")
            return
        if current < c and stayed > 0:
            print("impossible")
            return
    if current != 0:
        print("impossible")
        return
        
    print("possible")
helper(n)