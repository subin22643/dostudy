for t in range(1, 11):
    n = int(input())
    text = input()
    lst = []
    for i in text:
        if i != '+':
            lst.append(i)
        if len(lst) > 1:
            a = int(lst.pop())
            b = int(lst.pop())
            lst.append(a+b)
    print(f'#{t}', *lst)