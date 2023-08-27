T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    num = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                line = i+j+k
                if i >= 1 and j >= 1 and k >= 1 and line == N:
                    num.append([i, j, k])
    min_cnt = 9999
    for n in num:
        cnt = 0
        for l in range(M):
            for ii in range(n[0]):
                if lst[ii][l] != 'W':
                    cnt += 1
            for jj in range(n[0], n[0]+n[1]):
                if lst[jj][l] != 'B':
                    cnt += 1
            for kk in range(n[0]+n[1], n[0]+n[1]+n[2]):
                if lst[kk][l] != 'R':
                    cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt
    print(f'#{t}',min_cnt)