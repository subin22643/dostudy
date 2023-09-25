def MaxScore(flag = 0, cnt = 0, score = 0):
    global max_score
    if cnt == N:
        max_score = max(max_score, score)
        return
    for i in range(N):
        if (flag & (1<<i)) == 0:
            MaxScore((flag | (1<<i)), cnt + 1, score + MAP[cnt][i])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    MaxScore()
    print(f'#{t}', max_score)