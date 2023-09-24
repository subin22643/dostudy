def MinExpense(flag = 0, cnt = 0, cost = 0):
    global min_cost
    if cnt == N:
        min_cost = min(min_cost, cost)
    if cost > min_cost:
        return
    else:
        for i in range(N):
            if (flag & (1<<i)) == 0:
                MinExpense((flag | (1<<i)), cnt + 1, cost+lst[cnt][i])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    min_cost = float('inf')
    MinExpense()
    print(f'#{t}',min_cost)