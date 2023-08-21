T = int(input())
# 좌하우상 순서로 델타 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            point = MAP[i][j]
            max_side = 0    # 인접 지역 중 가장 높은 곳
            for k in range(4):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:       # 인접지역이 지도 범위 안에 있을 때
                    if max_side <= MAP[i+di[k]][j+dj[k]]:
                        max_side = MAP[i + di[k]][j + dj[k]]

            if point > max_side:    # 현재 위치가 인접 지역 중 가장 높은 곳보다 높다면
                cnt += 1

    print(f'#{t}', cnt)
