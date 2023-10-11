T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))

    dis = []

    water1 = 0
    water2 = 0
    tall_tree = max(tree)
    for tr in tree:
        dis.append(tall_tree-tr)

    for d in dis:
        water2 += d // 2
        water1 += d % 2
    day = 0
    while water1+1 < water2:
        water1 += 2
        water2 -= 1

    if water1 > water2:
        day += (water1*2) -1
    else:
        day += water2*2

    print(f'#{t}',day)
    
