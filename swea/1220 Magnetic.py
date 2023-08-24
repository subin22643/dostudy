def rec(lst):
    global cnt
    if len(lst) == 1 or (1 in lst and not 2 in lst) or (2 in lst and not 1 in lst):
        return
    for k in range(len(lst)):
        if lst[k] == 1:
            for l in range(k+1, len(lst)):
                if lst[l] == 2:
                    cnt += 1
                    for n in range(l+1):
                        lst.pop(0)
                    rec(lst)
                    return

for t in range(1, 11):
    input()
    lst = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0

    for j in range(100):
        magnet = []
        for i in range(100):
            if lst[i][j] != 0:
                magnet.append(lst[i][j])
        if magnet[0] == 2:
            magnet.pop(0)
        elif magnet[-1] == 1:
            magnet.pop()

        if len(magnet) > 1:
            rec(magnet)
    print(f'#{t}', cnt)