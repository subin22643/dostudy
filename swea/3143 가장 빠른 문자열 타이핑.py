T = int(input())

for t in range(1, T+1):
    A, B = list(input().split())

    print(f'#{t}', len(A)-((len(B)-1)*A.count(B)))