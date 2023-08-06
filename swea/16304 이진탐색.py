def search(end, page):
    count = 0
    start = 1
    while start <= end:
        middle = (start+end) // 2
        count += 1
        if middle == page:
            break
        elif middle < page:
            start = middle
        else:
            end = middle
    return count

T = int(input())
for t in range(1, T + 1):
    end, a, b = map(int, input().split())
    count_a = search(end, a)
    count_b = search(end, b)

    if count_a < count_b:
        print(f'#{t}', "A")
    elif count_a == count_b:
        print(f'#{t}', "0")
    else:
        print(f'#{t}', "B")

