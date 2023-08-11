T = 10
for t in range(1, T+1):
    N, str = list(input().split())
    lst = []

    for n in range(int(N)):
        lst.append(str[n])

        if len(lst) > 1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()
    print(f'#{t}',''.join(lst))