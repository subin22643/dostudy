N, M = map(int, input().split())

lst = []

for n in range(2 * N):
    lst.append(list(map(int, input().split())))

list_b = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        list_b[i][j] = lst[i][j] + lst[i+N][j]

for i in list_b:
    print(*i)