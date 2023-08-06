T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    lst = []
    max_sum = 0
    for n in range(N):
        lst.append(list(map(int, input().split())))

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            for k in range(M):
                for l in range(M):
                    sum_fly += lst[i+k][j+l]

            if max_sum < sum_fly:
                max_sum = sum_fly
    print(f'#{t}', max_sum)

