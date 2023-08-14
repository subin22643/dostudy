T = int(input())

lst = []
for _ in range(T):
    lst.append(int(input()))
    if lst[-1] == 0:
        lst.pop()
        lst.pop()

print(sum(lst))