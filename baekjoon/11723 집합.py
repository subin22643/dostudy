import sys
input = sys.stdin.readline

M = int(input())
S = set()
for m in range(M):
    lst = list(input().split())

    if lst[0] == 'add':
        S.add(int(lst[1]))
    elif lst[0] == 'remove':
        S.discard(int(lst[1]))
    elif lst[0] == 'check':
        if int(lst[1]) in S:
            print('1')
        else:
            print('0')
    elif lst[0] == 'toggle':
        if int(lst[1]) in S:
            S.remove(int(lst[1]))
        else:
            S.add(int(lst[1]))
    elif lst[0] == 'all':
        S.update(range(1, 21))
    elif lst[0] == 'empty':
        S = set()