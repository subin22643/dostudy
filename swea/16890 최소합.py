def route(i, j, num):
    global result
    if i == N-1 and j == N-1:
        result = min(result, num)
        return
    if 0 <= i+1 < N:
        route(i+1, j, num+lst[i+1][j])
    if 0 <= j+1 < N:
        route(i, j+1, num+lst[i][j+1])


T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    result = float("inf")
    route(0,0,lst[0][0])

    print(f'#{t}', result)