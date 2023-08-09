T = int(input())

for t in range(1, T+1):
    string = input()

    lst = []
    for i in string:
        if i == '(':
            lst.append(i)
        if i == '[':
            lst.append(i)
        if i == '{':
            lst.append(i)
        if i == ')':
            if lst and lst[-1] == '(':      # 리스트에 값이 존재하고 & 마지막 문자가 (이면
                lst.pop()
            else:
                lst.append(i)
                break
        if i == ']':
            if lst and lst[-1] == '[':
                lst.pop()
            else:
                lst.append(i)
                break
        if i == '}':
            if lst and lst[-1] == '{':
                lst.pop()
            else:
                lst.append(i)
                break

    if lst == []:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)