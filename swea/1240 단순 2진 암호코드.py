T = int(input())
for C in range(1, T+1):
    N, M = map(int, input().split())
    code = []
    for n in range(N):
        num = list(map(int, input()))
        if 1 in num and num[num.index(1) + 54] == 1:
            lst = list(num[num.index(1)-1:num.index(1) + 55])
        elif 1 in num and num[num.index(1) + 53] == 1:
            lst = list(num[num.index(1)-2:num.index(1) + 54])
        elif 1 in num and num[num.index(1) + 52] == 1:
            lst = list(num[num.index(1)-3:num.index(1) + 53])

    for i in range(8):
        number = []
        for j in range(7):
            number.append(lst.pop(0))
        numm = ''.join(map(str,number))

        if numm == '0001101':
            code.append(0)
        elif numm == '0011001':
            code.append(1)
        elif numm == '0010011':
            code.append(2)
        elif numm == '0111101':
            code.append(3)
        elif numm == '0100011':
            code.append(4)
        elif numm == '0110001':
            code.append(5)
        elif numm == '0101111':
            code.append(6)
        elif numm == '0111011':
            code.append(7)
        elif numm == '0110111':
            code.append(8)
        elif numm == '0001011':
            code.append(9)

    odd = 0
    even = 0

    for c in range(8):
        if (c+1) % 2 == 1:
            odd += code[c]
        else:
            even += code[c]

    if ((odd*3) + even) % 10 == 0:
        print(f'#{C}', odd+even)
    else:
        print(f'#{C} 0')