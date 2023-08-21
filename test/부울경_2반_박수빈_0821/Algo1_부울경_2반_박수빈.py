T = int(input())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    max_pang = 0
    min_pang = 999999999999999

    for i in range(N):
        for j in range(N):
            pang = lst[i][j]                # 기준점을 pang으로 지정
            for k in range(4):
                for l in range(1, lst[i][j]+1):     # 기준점에서 나온 수에 따라
                    ni = i + di[k]*l                # 델타 탐색 범위를 늘림
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N: # 탐색 범위가 게임판 내 일때만
                        pang += lst[ni][nj]         # 기준점에 점수 더하기
            if max_pang <= pang:            # 더해진 점수 중 가장 큰 수 추출
                max_pang = pang
            if min_pang >= pang:            # 더해진 점수 중 가장 작은 수 추출
                min_pang = pang
    bonus_score = max_pang - min_pang       # 가장 큰 수 - 가장 작은 수 = 얻을 수 있는 최대 점수
    print(f'#{t}', bonus_score)