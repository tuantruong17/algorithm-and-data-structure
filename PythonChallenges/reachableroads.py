num_cases = int(input())
for case in range(num_cases):
    m = int(input())
    neighbor = [set([]) for _ in range(m)]
    r = int(input())
    for i in range(r):
        src, dst = map(int, input().split())
        neighbor[src].add(dst)
        neighbor[dst].add(src)
        
    visited = [False] * m
    res = 0
    for i in range(m):
        if not visited[i]:
            visited[i] = True
            bfs = set([i])
            while len(bfs) != 0:
                new_bfs = set([])
                for v in bfs:
                    for v_neighbor in neighbor[v]:
                        if not visited[v_neighbor]:
                            visited[v_neighbor] = True
                            new_bfs.add(v_neighbor)
                bfs = new_bfs
            res += 1
    print(res - 1 if res != 0 else 0)
    