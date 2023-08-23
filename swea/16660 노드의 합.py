def tree(L):
    if not nodes[L]:
        if nodes[L*2] and N < L*2+1:
            nodes[L] = nodes[L*2]
        else:
            nodes[L] = tree(L*2) + tree(L*2+1)
    return nodes[L]

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N+1)

    for n in range(M):
        node = list(map(int, input().split()))
        nodes[node[0]] = node[1]

    result = tree(L)
    print(f'#{t}', result)




###
# T = int(input())
# for t in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0] * (N+1)
#     for _ in range(M):
#         a, b = map(int,input().split())
#         tree[a] = b
#     for i in range(N-M, 0, -1):
#         if i*2 == N:
#             tree[i] = tree[i*2]
#         else:
#             tree[i] = tree[i * 2] + tree[i * 2 + 1]
#     print(f'#{t} {tree[L]}')