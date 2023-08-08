T = int(input())

for t in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    max_count = 0
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1

        if max_count <= count:
            max_count = count
    print(f'#{t}', max_count)