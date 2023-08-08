T = int(input())

for t in range(1, T+1):
    lst = []
    for _ in range(9):
        lst.append(list(map(int, input().split())))
    cnt = 0
    for i in range(9):
        for j in range(1, 10):
            a = lst[i].count(j)
            if a == 1:
                pass
            else:
                cnt += 1

    for j in range(9):
        col = []
        for i in range(9):
            col.append(lst[i][j])
        for k in range(1, 10):
            a = col.count(k)
            if a == 1:
                pass
            else:
                cnt += 1

    for c in range(3):
        for d in range(3):
            squ = []
            for i in range(0+(3*c), 3+(3*c)):
                for j in range(0+(3*d), 3+(3*d)):
                    squ.append(lst[i][j])
            for k in range(1, 10):
                a = squ.count(k)

                if a == 1:
                    pass
                else:
                    cnt += 1

    if cnt == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')