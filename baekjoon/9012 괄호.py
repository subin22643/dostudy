T = int(input())

for t in range(1, T+1):
    text = input()

    lst = []
    for i in text:
        lst.append(i)

        if len(lst) > 1:
            if lst[-1] == ')' and lst[-2] == '(':
                lst.pop()
                lst.pop()

    if lst == []:
        print('YES')
    else:
        print('NO')