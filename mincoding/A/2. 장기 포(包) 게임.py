def dfs(x, y):
    global eat
    global move

    if move == 3:
        return

    # 위로 탐색
    po = 0
    for a in range(x-1, -1, -1):
        if po == 1:
            move += 1
            if MAP[a][y] == 1 and ate[a][y] == 0:
                eat += 1
                ate[a][y] = 1
                MAP[a][y] = 0
                dfs(a, y)
                MAP[a][y] = 1
            else:
                dfs(a, y)
            move -= 1
        if MAP[a][y] == 1:
            po += 1
        if po > 1:
            break

    # 아래로 탐색
    po = 0
    for b in range(x+1, N):
        if po == 1:
            move += 1
            if MAP[b][y] == 1 and ate[b][y] == 0:
                eat += 1
                ate[b][y] = 1
                MAP[b][y] = 0
                dfs(b, y)
                MAP[b][y] = 1
            else:
                dfs(b, y)
            move -= 1
        if MAP[b][y] == 1:
            po += 1
        if po > 1:
            break

    # 왼쪽으로 탐색
    po = 0
    for c in range(y-1, -1, -1):
        if po == 1:
            move += 1
            if MAP[x][c] == 1 and ate[x][c] == 0:
                eat += 1
                ate[x][c] = 1
                MAP[x][c] = 0
                dfs(x, c)
                MAP[x][c] = 1
            else:
                dfs(x, c)
            move -= 1
        if MAP[x][c] == 1:
            po += 1
        if po > 1:
            break

    # 오른쪽으로 탐색
    po = 0
    for d in range(y+1, N):
        if po == 1:
            move += 1
            if MAP[x][d] == 1 and ate[x][d] == 0:
                eat += 1
                ate[x][d] = 1
                MAP[x][d] = 0
                dfs(x, d)
                MAP[x][d] = 1
            else:
                dfs(x, d)
            move -= 1
        if MAP[x][d] == 1:
            po += 1
        if po > 1:
            break


T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    eat = 0
    move = 0
    ate = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                MAP[i][j] = 0
                ii = i
                jj = j
                break
    dfs(ii, jj)
    print(f'#{t}',eat)