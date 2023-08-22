def integer(x):
    if x - int(x) > 0:
        return int(x) + 1
    return int(x)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N+1)]

    house = []
    max_dis = 0     # (가장 먼 집까지의 거리)^2
    for i in range(N+1):
        for j in range(N+1):
            if MAP[i][j] == 2:
                rpt = [i, j]
            elif MAP[i][j] == 1:
                house.append([i,j])

    for h in range(len(house)):
        distance = (house[h][0] - rpt[0])**2 + (house[h][1] - rpt[1])**2
        if max_dis < distance**0.5:
            max_dis = distance**0.5

    result = integer(max_dis)
    print(f'#{t}', result)