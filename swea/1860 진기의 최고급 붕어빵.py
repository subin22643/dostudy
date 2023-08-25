T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    per = list(map(int, input().split()))
    per.sort()

    result = 1
    bread = 0

    if 0 in per:
        result = 0
    else:
        for sec in range(1, 11112):  # 지금 몇초인지
            if sec % M ==0:
                bread += K
            for p in per:       # 사람 오는 시간
                if sec == p:
                    if bread >= 1:
                        bread -= 1
                    else:
                        result = 0
                        break

    if result == 1:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Impossible')