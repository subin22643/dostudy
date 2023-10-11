T = int(input())
for t in range(1, T+1):
    # 시드액, 매달 추가금
    Ms, Ma = map(int, input().split())
    # 종목 수, 기간
    N, L = map(int, input().split())
    price = [list(map(int, input().split())) for _ in range(N)]

    # 가진 현금
    cash = Ms
    # 가진 주식의 종목 번호, 수량
    stock = []

    for l in range(L):
        # 매도
        if stock:
            for s in stock:
                cash += price[s[0]][l] * s[1]
        stock = []

        # 매수
        profit = [0] * N    # 종목별 다음달과 시세 차이
        ppp = [0] * N       # 종목별 가격 1당 수익 (profit per price)

        for n in range(N):
            profit[n] = price[n][l+1] - price[n][l]
            ppp[n] = profit[n] / price[n][l]
        sorted_ppp = sorted(ppp, reverse=True)

        for p in sorted_ppp:
            if p <= 0:
                break
            else:
                qty = cash // price[ppp.index(p)][l]    # 매수량
                cash -= price[ppp.index(p)][l] * qty    # 매수 후 현금
                stock.append([ppp.index(p), qty])       # 가진 주식
        cash += Ma
    # 반복문에서 (L-1)번째 달의 매수 리스트 처리가 안 되기 때문에 따로 한 번 더 계산
    if stock:
        for s in stock:
            cash += price[s[0]][L] * s[1]

    # 투자금
    inv = Ms + Ma*L

    print(f'#{t}',cash-inv)