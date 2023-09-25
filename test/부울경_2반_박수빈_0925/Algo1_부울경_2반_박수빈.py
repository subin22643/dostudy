T = int(input())
for t in range(1, T+1):
    N = int(input())
    P = list(input())
    key = input()

    H = ''
    for i in range(N):
        if P[i] == 'A':
            P[i] = 10
        elif P[i] == 'B':
            P[i] = 11
        elif P[i] == 'C':
            P[i] = 12
        elif P[i] == 'D':
            P[i] = 13
        elif P[i] == 'E':
            P[i] = 14
        elif P[i] == 'F':
            P[i] = 15
        else:
            P[i] = int(P[i])

        if key == 'A':
            key = 10
        elif key == 'B':
            key = 11
        elif key == 'C':
            key = 12
        elif key == 'D':
            key = 13
        elif key == 'E':
            key = 14
        elif key == 'F':
            key = 15
        else:
            key = int(key)

        if P[i] >= 10 and key >= 10:
            num = (P[i]-key) % 16
        else:
            num = (P[i] + key) % 16

        if num == 10:
            H += 'A'
        elif num == 11:
            H += 'B'
        elif num == 12:
            H += 'C'
        elif num == 13:
            H += 'D'
        elif num == 14:
            H += 'E'
        elif num == 15:
            H += 'F'
        else:
            H += str(num)

    print(f'#{t}', H)