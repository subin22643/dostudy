def dfs(net, start, visited):
    visited[start] = 1
    for n in net[start]:
        if visited[n] == 0:
            dfs(net, n, visited)

for _ in range(1, 11):
    t, N = map(int, input().split())
    lst = list(map(int, input().split()))

    net = [[] for _ in range(100)]

    for i in range(N):
        net[lst[i*2]].append(lst[i*2+1])

    visited = [0] * 100
    dfs(net, 0, visited)

    if visited[99] == 1:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')