T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    blank = []
    for i in range(N):
        length = 1
        for j in range(N-1):
            if lst[i][j] == 1 and lst[i][j+1] == 1:
                length += 1
                if j == N-2:
                    blank.append(length)
                    length = 1
            elif lst[i][j] == 1 and lst[i][j+1] == 0:
                blank.append(length)
                length = 1
            elif lst[i][j] == 0:
                length = 1
    ls = list(zip(*lst))
    for i in range(N):
        length = 1
        for j in range(N-1):
            if ls[i][j] == 1 and ls[i][j+1] == 1:
                length += 1
                if j == N-2:
                    blank.append(length)
                    length = 1
            elif ls[i][j] == 1 and ls[i][j+1] == 0:
                blank.append(length)
                length = 1
            elif ls[i][j] == 0:
                length = 1

    print(f'#{t}', blank.count(K))