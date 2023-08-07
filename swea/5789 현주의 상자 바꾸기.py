T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())

    lst = [0]*N

    for q in range(Q):
        L, R = map(int, input().split())

        for i in range(L-1, R):
            lst[i] = q+1
    print(f'#{t}', *lst)

