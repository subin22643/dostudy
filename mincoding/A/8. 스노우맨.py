def bfs(limit):
    visited = [[0] * M for _ in range(N)]
    visited[start_i][start_j] = 1
    q = [(start_i, start_j)]

    while q:
        i, j = q.pop(0)

        for k in range(4):
            if k < 2:
                for l in range(1, limit+1):
                    ni = i + di[k]*l
                    nj = j
                    if 0<=ni<N and visited[ni][nj] == 0:
                        if MAP[ni][nj] == 1:
                            visited[ni][nj] = 1
                            q.append((ni,nj))
                        elif MAP[ni][nj] == 3:
                            return 1
            else:
                ni = i
                nj = j + dj[k]
                if 0<=nj<M and visited[ni][nj] == 0:
                    if MAP[ni][nj] == 1:
                        visited[ni][nj] = 1
                        q.append((ni,nj))
                    elif MAP[ni][nj] == 3:
                        return 1
    return 0

di = [1, -1, 0,0]
dj = [0,0,1,-1]
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            start_i = i
            start_j = j
            break
for n in range(N):
    if bfs(n):
        print(n)
        break
