T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
 
    sum_list = []
    for i in range(0, N-M+1):    # lst 대신 range(1, N-M) 가능?
        sum_num = 0
        for j in range(i, i+M):
            sum_num += lst[j]

        sum_list.append(sum_num)
        
    min_v = min(sum_list)
    max_v = max(sum_list)
    result = max_v - min_v
    print(f'#{tc}', result)