T = int(input())

for t in range(1, T+1):
    lst = []
    result = 0
    text = input().split()
    for i in text:
        if i == '.':
            if len(lst) == 1:
                break
            else:
                result = -1
                break
        elif i not in '+-*/':
            lst.append(int(i))
        elif i == '+':
            if len(lst) > 1:
                a = lst.pop()
                b = lst.pop()
                lst.append(a+b)
            else:
                result = -1
                break
        elif i == '-':
            if len(lst) > 1:
                a = lst.pop()
                b = lst.pop()
                lst.append(b-a)
            else:
                result = -1
                break

        elif i == '*':
            if len(lst) > 1:
                a = lst.pop()
                b = lst.pop()
                lst.append(a * b)
            else:
                result = -1
                break

        elif i == '/':
            if len(lst) > 1:
                a = lst.pop()
                b = lst.pop()
                if b == 0:
                    result = -1
                else:
                    lst.append(b // a)
            else:
                result = -1
                break
    if result == -1:
        print(f'#{t}', "error")
    else:
        print(f'#{t}', *lst)