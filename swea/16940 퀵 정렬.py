def hoare_partition(lst, start, end):
    pivot = lst[start]
    i = start
    j = end
    while i <= j:
        while i <= j and lst[i] <= pivot:
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[start], lst[j] = lst[j], lst[start]
    return j

def quick_sort(lst, start, end):
    if start < end:
        s = hoare_partition(lst, start, end)
        quick_sort(lst, start, s-1)
        quick_sort(lst, s+1, end)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, len(lst)-1)

    print(f'#{t}',lst[N//2])