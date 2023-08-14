T = int(input())
cnt = 0
for _ in range(T):
    text = input()

    lst = []
    for t in range(len(text)):
        lst.append(text[t])
        if len(lst) >= 2:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()

    if lst == []:
        cnt += 1

print(cnt)