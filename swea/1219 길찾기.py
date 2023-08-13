for _ in range(10):
    t, N = map(int, input().split())
    lst = list(map(int, input().split()))

    visited = [False] * 100
    stack = []

    arr1 = [0] * 100
    arr2 = [0] * 100

    for i in range(0, N*2, 2):
        if arr1[lst[i]] == 0:
            arr1[lst[i]] = lst[i+1]
        else:
            arr2[lst[i]] = lst[i+1]

    vertex = 0
    visited[vertex] = True
    result = 0

    while True:
        if visited[99]:
            result = 1
            break

        if arr1[vertex] != 0 and visited[arr1[vertex]] == False:
            stack.append(vertex)
            visited[arr1[vertex]] = True
            vertex = arr1[vertex]

        elif arr2[vertex] != 0 and visited[arr2[vertex]] == False:
            stack.append(vertex)
            visited[arr2[vertex]] = True
            vertex = arr2[vertex]

        if visited[arr1[vertex]] == True and visited[arr2[vertex]] == True:
            vertex = stack[-1]
            stack.pop()

            if stack == [] and visited[arr1[vertex]] == True and visited[arr2[vertex]]:
                break
    print(f'#{t}', result)