T = int(input())
for t in (1, T+1):
    N = int(input())

    lst = [0] * 5000

    for i in range(N):
        a, b = map(int, input().split())

        for j in range(a,b+1):
            lst[j] += 1

    P = int(input())
    blank_list = []
    for k in range(P):
        a = int(input())
        blank_list.append(lst[a])

    print(f'#{t}', *blank_list)




