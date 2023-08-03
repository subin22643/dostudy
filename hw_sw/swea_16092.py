T  = int(input())

for tc in range(1, T+1):
    num = int(input())
    lst = list(map(int, input().split()))

    min_v = lst[0]
    max_v = lst[0]

    for i in lst:
        if min_v > i:
            min_v = i

    for i in lst:
        if max_v < i:
            max_v = i
    
    diff = max_v - min_v
    print(f'#{tc} {diff}')