T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))

    all = []
    for n in range(1, N+1):
        all.append(n)

    for k in range(K):
        all.remove(num[k])
    print(f'#{t}', *all)