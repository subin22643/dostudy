while True:
    text = list(input())
    if text[0] == '.':
        break
    lst = []
    for i in range(len(text)):
        if text[i] == '(':
            lst.append(text[i])
        if text[i] == '[':
            lst.append(text[i])
        if text[i] == ')':
            lst.append(text[i])
            if len(lst) > 1:
                if lst[-1] == ')' and lst[-2] == '(':
                    lst.pop()
                    lst.pop()
                else:
                    break
        if text[i] == ']':
            lst.append(text[i])
            if len(lst) > 1:
                if lst[-1] == ']' and lst[-2] == '[':
                    lst.pop()
                    lst.pop()
                else:
                    break
    if lst == []:
        print('yes')
    else:
        print('no')