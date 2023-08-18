def bfs(start):
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    q = []
    q.append(start)

    while q:
        w = q.pop(0)
        if maze[w[0]][w[1]] == 3:
            return visited[w[0]][w[1]] -2
        for k in range(4):
            ni = w[0]+di[k]
            nj = w[1]+dj[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[w[0]][w[1]] + 1

    return 0

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = []

    tmp = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start.append(i)
                start.append(j)
                tmp = 1
                break
        if tmp:
            break

    result = bfs(start)
    print(f'#{t}', result)