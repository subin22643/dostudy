T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    lst = []
    for _ in range(N):
        lst.append(list(input()))

    palin = []
    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            for k in range(M//2):
                if lst[i][j+k] == lst[i][j+M-1-k]:
                    cnt += 1
            if cnt == M//2:
                for l in range(M):
                    palin.append(lst[i][j+l])

    for j in range(N):
        for i in range(N-M+1):
            cnt = 0
            for k in range(M//2):
                if lst[i+k][j] == lst[i+M-1-k][j]:
                    cnt += 1
            if cnt == M//2:
                for l in range(M):
                    palin.append(lst[i+l][j])

    print(f'#{t}',''.join(palin))