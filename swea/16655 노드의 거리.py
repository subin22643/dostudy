def node(S, G):
    visited = [0] * 51
    q = []
    visited[S] = 1
    q.append(S)

    while q:
        w = q.pop(0)
        if w == G:
            return visited[w] -1
        for i in lst[w]:
            if visited[i] == 0:
                visited[i] = visited[w] + 1
                q.append(i)

    return 0



T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(51)]

    for _ in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    S, G = map(int, input().split())

    result = node(S, G)
    print(f'#{t}', result)