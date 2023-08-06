T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    N, M = map(int, input().split())

    lst = []
    for n in range(N):
        lst.append(list(map(int, input().split())))

    max_sum = 0
    for i in range(N):
        for j in range(M):
            flower = lst[i][j]
            for k in range(4):
                    if 0<= i+di[k] <N and 0<= j+dj[k] < M:
                        flower += lst[i+di[k]][j+dj[k]]
            if max_sum < flower:
                max_sum = flower
    print(max_sum)

