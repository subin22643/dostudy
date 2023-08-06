T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    for n in range(N):
        lst.append(list(map(int, input().split())))

    max_fly = 0
    for a in range(0, N-M+1):    # a랑 b는 파리채 기준점
        for b in range(0, N-M+1):
            fly = 0
            for i in range(M):    # i랑 j는 파리채 때리는 범위
                for j in range(M):
                    # if 0 <= a + i < N and 0 <= b + j < N:    # 범위 지정(range(0,N-M+1)) 제대로 돼서 안넣어도됨
                        fly += lst[a+i][b+j]
            if max_fly <= fly:
                max_fly = fly
    print(f'#{t}', max_fly)