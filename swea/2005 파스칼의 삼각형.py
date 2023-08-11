T = int(input())

for t in range(1, T+1):
    N = int(input())

    lst = [[0] * N for _ in range(N)]

    for i in range(N):
        lst[i][0] = 1
        for j in range(i+1):
            if i-1 >= 0 and j-1 >= 0:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    print(f'#{t}')

    for i in range(N):
        for j in range(i+1):
            if lst[i][j] != 0:
                print(lst[i][j], end = ' ')
        print()
