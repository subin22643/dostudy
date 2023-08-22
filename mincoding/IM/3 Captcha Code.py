T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    start = 0

    for i in range(K):
        if passcode[i] in sample:
            for k in range(sample.index(passcode[i])+1):
                sample.pop(0)
        else:
            sample = []
            break

    if sample:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')