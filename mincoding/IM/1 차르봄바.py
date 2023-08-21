T = int(input())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for t in range(1, T+1):
    N, P = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_virus = 0

    for i in range(N):
        for j in range(N):
            virus = MAP[i][j]
            for k in range(4):
                for l in range(1, P+1):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0<= nj < N:
                        virus += MAP[ni][nj]
            if max_virus < virus:
                max_virus = virus
    print(f'#{t}', max_virus)