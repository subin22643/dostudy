def route(start):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append(start)
    visited[start[0]][start[1]] = 1

    while q:
        w = q.pop(0)
        if lst[w[0]][w[1]] == '3':
            return 1
        for k in range(4):
            ni = w[0] + di[k]
            nj = w[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] != '1' and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1
    return 0

T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for t in range(1, T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if lst[i][j] == '2':
                start = [i, j]

    result = route(start)
    print(f'#{t}', result)