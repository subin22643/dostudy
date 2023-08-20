lst = [list(map(int, input().split())) for _ in range(7)]

visited = [[0] * 7 for __ in range(7)]
q = []

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
color = 0

for i in range(7):
    for j in range(7):
        cnt = 0
        q.append([i, j])
        while q:
            w = q.pop(0)        # w = [1, 1]
            for k in range(4):
                ni = w[0]+di[k]
                nj = w[1]+dj[k]
                if 0 <= ni < 7 and 0 <= nj < 7 and visited[ni][nj] == 0 and lst[i][j] == lst[ni][nj]:
                    cnt += 1
                    q.append([ni, nj])
                    visited[ni][nj] = 1
        if cnt >= 3:
            color += 1
print(color)