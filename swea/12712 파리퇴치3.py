T = int(input())
di1 = [0, 1, 0, -1]     # + 모양일때
dj1 = [1, 0, -1, 0]
di2 = [-1, 1, 1, -1]    # x 모양일때
dj2 = [1, 1, -1, -1]

for t in range(1, T+1):
    N, M = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    for i in range(N):
        for j in range(N):
            fly_plus = lst[i][j]
            fly_x = lst[i][j]
            for k in range(1, M):
                for l in range(4):
                    if 0 <= i+(di1[l]*k) < N and 0 <= j+(dj1[l]*k) < N:
                        fly_plus += lst[i+(di1[l]*k)][j+(dj1[l]*k)]

                    if 0 <= i+(di2[l]*k) < N and 0 <= j+(dj2[l]*k) < N:
                        fly_x += lst[i+(di2[l]*k)][j+(dj2[l]*k)]

                    if max <= fly_plus:
                        max = fly_plus
                    if max <= fly_x:
                        max = fly_x

    print(f'#{t}', max)