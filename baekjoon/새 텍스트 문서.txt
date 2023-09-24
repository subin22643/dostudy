import sys
input = sys.stdin.readline

M = int(input())
S = 0
for m in range(M):
    lst = list(input().split())

    if lst[0] == 'add':
        if not S & (1<<(int(lst[1]) -1)):
            S += (1 << (int(lst[1]) -1))
    elif lst[0] == 'remove':
        if S & (1<<(int(lst[1]) -1)):
            S -= (1 << (int(lst[1]) -1))
    elif lst[0] == 'check':
        if S & (1<<(int(lst[1]) -1)):
            print('1')
        else:
            print('0')
    elif lst[0] == 'toggle':
        if S & (1<<(int(lst[1]) -1)):
            S -= (1 << (int(lst[1]) -1))
        else:
            S += (1 << (int(lst[1]) -1))
    elif lst[0] == 'all':
        S = (1<<20)-1
    elif lst[0] == 'empty':
        S = 0