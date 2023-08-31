def babygin(lst):
    per1 = [0] * 10
    per2 = [0] * 10
    result = 0
    flag = 0
    for n in range(len(lst)):
        if n % 2 == 0:
            per1[lst.pop(0)] += 1
        else:
            per2[lst.pop(0)] += 1

        for i in range(10):
            if per1[i] == 3 or (0<=i<=7 and per1[i] > 0 and per1[i+1] > 0 and per1[i+2] > 0):
                result = 1
                flag = 1
                break
            if per2[i] == 3 or (0<=i<=7 and per2[i] > 0 and per2[i+1] > 0 and per2[i+2] > 0):
                result = 2
                flag = 1
                break
        if flag:
            break
    print(f'#{t}', result)


T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    babygin(lst)