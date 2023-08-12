T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if lst[i][j] == 1:
                cnt += 1
            else:
                cnt = 0

            if max_cnt <= cnt:
                max_cnt = cnt

    for j in range(M):
        cnt = 0
        for i in range(N):
            if lst[i][j] == 1:
                cnt += 1
            else:
                cnt = 0

            if max_cnt <= cnt:
                max_cnt = cnt
    print(f'#{t} {max_cnt}')