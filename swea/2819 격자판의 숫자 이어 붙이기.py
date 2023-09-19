def dfs(i, j, num):
    if len(num) == 7:
        if num not in numbers:
            numbers.append(num)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni,nj, num + lst[ni][nj])


T = int(input())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for t in range(1, T+1):
    lst = [list(input().split()) for _ in range(4)]

    numbers = []
    for i in range(4):
        for j in range(4):
            num = lst[i][j]
            dfs(i, j, num)

    print(f'#{t}', len(numbers))