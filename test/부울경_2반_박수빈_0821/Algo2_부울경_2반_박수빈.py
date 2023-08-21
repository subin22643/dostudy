T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(input().split())       # A 카드덱
    B = []                          # B 카드덱
    C = []                          # C 카드덱
    bonus = 0                       # 보너스 숫자
    for a in A:                     # A 카드덱 안에 있는 카드가
        if a.isdecimal():           # 숫자이면
            if (int(a)+bonus) % 2 == 1:     # 카드의 숫자+보너스숫자가 홀수이면
                B.append(int(a)+bonus)      # B 카드덱에 추갸
            else:                           # 카드의 숫자+보너스숫자가 짝수이면
                C.append(int(a)+bonus)      # C 카드덱에 추가
        else:                       # 숫자가 아니면 = '+'이면
            bonus += 1              # 보너스 숫자 1 증가

    for m in range(M):              # 김싸피의 순서 M이 될때까지
        if B:                       # B 카드덱에 카드가 있다면
            B_ssafy = B.pop(0)      # 선입선출 방식으로 카드 가져감
        else:                       # B 카드덱에 카드가 없다면
            B_ssafy = 0             # B 카드덱에서 얻은 싸피의 점수는 0
        if C:                       # C 카드덱에 카드가 있다면
            C_ssafy = C.pop()       # 후입선출 방식으로 카드 가져감
        else:                       # C 카드덱에 카드가 없다면
            C_ssafy = 0             # C 카드덱에서 얻은 싸피의 점수는 0

    print(f'#{t}', B_ssafy + C_ssafy)   # B 카드덱에서 얻은 싸피의 점수 + C 카드덱에서 얻은 싸피의 점수