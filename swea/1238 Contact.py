def bfs(start):
    visited = [0] * 101
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        w = q.pop(0)
        for i in net[w]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[w] + 1
    MAX = 0
    result = 0
    for i in range(1, 101):
        if MAX <= visited[i]:
            MAX = visited[i]
            result = i
    return result

for t in range(1, 11):
    num, start = map(int, input().split())
    lst = list(map(int, input().split()))

    net = [[] for _ in range(101)]
    for i in range(len(lst) // 2):
        net[lst[i*2]].append(lst[i*2+1])


    result = bfs(start)
    print(f'#{t}', result)