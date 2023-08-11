T = int(input())

for t in range(1, T+1):
    text = input()
    lst = []

    for n in range(len(text)):
        lst.append(text[n])

        if len(lst) > 1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()

    print(f'#{t}',len(lst))