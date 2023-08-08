T = 10

for t in range(1, T+1):
    N = int(input())

    lst = []
    for _ in range(8):
        lst.append(list(input()))

    palin = 0
    for i in range(8):
        for j in range(8-N+1):
            cnt = 0
            for k in range(N//2):
                if lst[i][j+k] == lst[i][j+N-1-k]:
                    cnt += 1
            if cnt == N//2:
                palin += 1

    for j in range(8):
        for i in range(8-N+1):
            cnt = 0
            for k in range(N//2):
                if lst[i+k][j] == lst[i+N-1-k][j]:
                    cnt += 1
            if cnt == N//2:
                palin += 1
    print(f'#{t}', palin)