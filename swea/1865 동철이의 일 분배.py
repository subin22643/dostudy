def dfs(per = 1, cnt = 0):
    global result
    if cnt == N:
        result = max(per, result)
        return
    if result >= per:
        return
    for k in range(N):
        if not visited[k]:
            visited[k] = 1
            dfs(per * (lst[cnt][k]/100), cnt+1)
            visited[k] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    visited = [0] * N
    dfs()
    result = format(result * 100, '.6f')
    print(f'#{t} {result}')