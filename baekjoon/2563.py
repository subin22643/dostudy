T = int(input())
blank_list = [[0] * 100 for _ in range(100)]

for t in range(1, T+1):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            blank_list[i][j] = 1

count = 0
for k in range(100):
    for l in range(100):
        if blank_list[k][l] == 1:
            count += 1
print(count)