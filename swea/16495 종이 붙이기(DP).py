T = int(input())
for t in range(1, T+1):
    num = int(input()) // 10
    lst = [0, 1, 3]
    for i in range(3, num+1):
        lst.append(lst[i-2]*2 + lst[i-1])
    result = lst[num]
    print(f'#{t} {result}')