T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    max_cnt = 1
    for n in range(N):
        if n > 0:
            if lst[n] > lst[n-1]:
                cnt += 1
                if max_cnt <= cnt:
                    max_cnt = cnt
            else:
                cnt = 1
    print(f'#{t} {max_cnt}')