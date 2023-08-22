T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for i in range(N)]

    max_score = 0
    min_score = float("inf")

    for i in range(N):
        score = 0
        bonus = 0
        for j in range(M):
            if answer[j] == lst[i][j]:
                score += 1 + bonus
                bonus += 1
            else:
                bonus = 0
        if max_score < score:
            max_score = score
        if min_score > score:
            min_score = score

    interval = (max_score - min_score)
    print(f'#{t}', interval)