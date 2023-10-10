T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    apple = list([0,0] for _ in range(11))
    M = 0
    cnt = 1    # 1번 사과를 먹을때는 무조건 1번 꺾음
    for i in range(N):
        for j in range(N):
            if M < MAP[i][j]:
                M = MAP[i][j]
            if MAP[i][j] != 0:
                apple[MAP[i][j]] = [i,j]

    # 현재 방향: 우(0), 하(1), 좌(2), 상(3)
    direction = 3

    for a in range(1, 10):
        if a == M:
            break
        # 다음 사과가 좌상
        if apple[a][0] > apple[a+1][0] and apple[a][1] > apple[a+1][1]:
            # 우방향이면
            if direction == 0:
                direction = 1
                cnt += 1
            # 하방향이면
            elif direction == 1:
                direction = 0
                cnt += 3
            # 좌방향이면
            elif direction == 2:
                direction = 1
                cnt += 3
            # 상방향이면
            elif direction == 3:
                direction = 1
                cnt += 2

        # 다음 사과가 좌하
        elif apple[a][0] < apple[a + 1][0] and apple[a][1] > apple[a + 1][1]:
            # 우방향이면
            if direction == 0:
                direction = 3
                cnt += 3
            # 하방향이면
            elif direction == 1:
                direction = 0
                cnt += 3
            # 좌방향이면
            elif direction == 2:
                direction = 0
                cnt += 2
            # 상방향이면
            elif direction == 3:
                direction = 0
                cnt += 1

        # 다음 사과가 우상
        elif apple[a][0] > apple[a + 1][0] and apple[a][1] < apple[a + 1][1]:
            # 우방향이면
            if direction == 0:
                direction = 2
                cnt += 2
            # 하방향이면
            elif direction == 1:
                direction = 2
                cnt += 1
            # 좌방향이면
            elif direction == 2:
                direction = 1
                cnt += 3
            # 상방향이면
            elif direction == 3:
                direction = 2
                cnt += 3

        # 다음 사과가 우하
        elif apple[a][0] < apple[a + 1][0] and apple[a][1] < apple[a + 1][1]:
            # 우방향이면
            if direction == 0:
                direction = 3
                cnt += 3
            # 하방향이면
            elif direction == 1:
                direction = 3
                cnt += 2
            # 좌방향이면
            elif direction == 2:
                direction = 3
                cnt += 1
            # 상방향이면
            elif direction == 3:
                direction = 2
                cnt += 3

    print(f'#{t}', cnt)