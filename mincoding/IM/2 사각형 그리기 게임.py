T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    max_size = 0
    for i in range(N):
        for j in range(N):
            if (N-i)*(N-j) < max_size:
                break
            for k in range(N-i):
                for l in range(N-j):
                    if MAP[i][j] == MAP[i+k][j+l]:
                        size = (k+1) * (l+1)
                        if max_size < size:
                            max_size = size
                            cnt = 1
                        elif max_size == size:
                            cnt += 1
    print(f'#{t}', cnt)