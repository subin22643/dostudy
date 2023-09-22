def dfs(v):
    q = [v]
    stu[v] = True
    while q:
        w = q.pop(0)
        for k in group[w]:
            if not stu[k]:
                stu[k] = True
                q.append(k)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    group = [[] for _ in range(N+1)]

    for i in range(M):
        group[lst[i*2]].append(lst[i*2+1])
        group[lst[i*2+1]].append(lst[i*2])

    stu = [False] * (N+1)
    cnt = 0

    for j in range(1, N+1):
        if not stu[j]:
            dfs(j)
            cnt += 1
    print(cnt)