def dfs(start):
    visited[start[0]][start[1]] = 1
    if maze[start[0]][start[1]] == '3':
        return 1
    for k in range(4):
        ni = start[0] + di[k]
        nj = start[1] + dj[k]
        if 0<=ni<N and 0<=nj<N and maze[ni][nj] != '1' and visited[ni][nj] == 0:
            if dfs([ni,nj]) == 1:
                return 1
    return 0

T = int(input())
di = [0,0,1,-1]
dj = [1,-1,0,0]
for t in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = [i,j]
                result = dfs(start)
    print(f'#{t}', result)