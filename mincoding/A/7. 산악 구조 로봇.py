def bfs():
    q = [(0,0,0)]   # 현위치x, y, 연료량
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = 0
    min_fuel = float('inf')

    while q:
        i, j, fuel = q.pop(0)
        if i == N-1 and j == N-1:
            min_fuel = min(fuel, min_fuel)
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                dif = MAP[ni][nj] - MAP[i][j]
                if dif > 0:
                    new_fuel = fuel + dif*2
                elif dif == 0:
                    new_fuel = fuel +1
                else:
                    new_fuel = fuel

                if new_fuel < visited[ni][nj]:
                    visited[ni][nj] = new_fuel
                    q.append([ni,nj,new_fuel])

        for [a, b, c, d, e] in tunnel:
            if i == a-1 and j == b-1:
                new_fuel = fuel + e
                if new_fuel < visited[c-1][d-1]:
                    visited[c-1][d-1] = new_fuel
                    q.append([c-1, d-1, new_fuel])
            elif i == c-1 and j == d-1:
                new_fuel = fuel + e
                if new_fuel < visited[a-1][b-1]:
                    visited[a-1][b-1] = new_fuel
                    q.append([a-1, b-1, new_fuel])
    return min_fuel



di = [1, -1, 0, 0]
dj = [0,0,1,-1]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [list(map(int, input().split())) for _ in range(M)]

    re = bfs()
    print(f'#{t}', re)