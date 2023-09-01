T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    load = 0

    for t in range(len(truck)):
        for w in weight:
            if truck[t] >= w:
                load += w
                weight.remove(w)
                break

    print(f'#{tc}', load)