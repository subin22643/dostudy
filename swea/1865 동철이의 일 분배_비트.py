def MaxPer(flag = 0, cnt = 0, per = 1):
    global max_per
    if cnt == N:
        max_per = max(max_per, per)
        return
    if per <= max_per:
        return
    else:
        for i in range(N):
            if (flag & (1<<i)) == 0:
                MaxPer((flag | (1<<i)), cnt+1, per*(lst[cnt][i]/100))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_per = 0
    MaxPer()
    print(f'#{t}', format(max_per*100, '.6f'))