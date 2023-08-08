T = int(input())
st_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

lst = []
for _ in range(1, T+1):
    t, N = input().split()
    lst = list(input().split())

    for i in range(int(N)):
        for j in range(10):
            if lst[i] == st_lst[j]:
                lst[i] = j

    lst.sort()
    for i in range(int(N)):
        for j in range(10):
            if lst[i] == j:
                lst[i] = st_lst[j]
    print(t, *lst)