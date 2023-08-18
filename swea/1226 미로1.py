def route(start):
    visited = [[0] * 16 for _ in range(16)]
    q = []
    q.append(start)
    visited[start[0]][start[1]] = 1

    while q:
        w = q.pop(0)
        if maze[w[0]][w[1]] == 3:
            return visited[w[0]][w[1]]
        for k in range(4):
            ni = w[0] + di[k]
            nj = w[1] + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni,nj])
                visited[ni][nj] = 1
    return 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for _ in range(10):
    t = int(input())
    maze = [list(map(int, input())) for __ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]

    result = route(start)
    print(f'#{t}', result)