def tree(root):
    if node[root] == '-':
        node[root] = int(tree(edge[root][0])) - int(tree(edge[root][1]))
    elif node[root] == '+':
        node[root] = int(tree(edge[root][0])) + int(tree(edge[root][1]))
    elif node[root] == '/':
        node[root] = int(tree(edge[root][0])) / int(tree(edge[root][1]))
    elif node[root] == '*':
        node[root] = int(tree(edge[root][0])) * int(tree(edge[root][1]))
    else:
        node[root] == int(node[root])
    return node[root]

root = 1
for t in range(1, 11):
    N = int(input())

    node = [0] * (N+1)
    edge = [[] for __ in range(N+1)]

    for _ in range(N):
        n = input().split()
        node[int(n[0])] = n[1]

        if n[1] in '+-*/':
            edge[int(n[0])].append(int(n[2]))
            edge[int(n[0])].append(int(n[3]))

    result = int(tree(root))
    print(f'#{t}', result)