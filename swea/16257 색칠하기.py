T = int(input())
for t in range(1, T+1):
    N = int(input())

    empty_list = []
    for _ in range(10):    # 10*10 빈 리스트 만들기
        row = [0] * 10
        empty_list.append(row)

    lst = []
    count = 0
    for n in range(N):
        lst.append(list(map(int, input().split())))

        for i in range(lst[n][0], lst[n][2]+1):    # 빨간색 범위
            for j in range(lst[n][1], lst[n][3]+1):    # 파란색 범위
                if lst[n][4] == 1:                 # 빨간색 범위에 1 더하기
                    empty_list[i][j] += 1
                else:                              # 파란색 범위에 2 더하기
                    empty_list[i][j] += 2

                if empty_list[i][j] == 3:          # 값이 3이면 (빨강1 + 파랑2)이면 카운트
                    count += 1

    print(f'#{t}', count)