def tree(N):
    cnt = 1
    if ch1[N] != 0:
        cnt += tree(ch1[N])
    if ch2[N] != 0:
        cnt += tree(ch2[N])
    return cnt

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(E):
        if ch1[lst[i*2]] == 0:
            ch1[lst[i*2]]= lst[i*2+1]
        else:
            ch2[lst[i*2]] = lst[i * 2 + 1]

    result = tree(N)
    print(f'#{t}', result)