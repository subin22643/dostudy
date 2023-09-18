def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    if left_half[-1] > right_half[-1]:
        cnt += 1
    return merge(left_half, right_half)


def merge(left, right):
    global cnt
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    print(f'#{t}', merge_sort(lst)[N//2], cnt)