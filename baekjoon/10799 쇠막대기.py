pipe = list(input())

lst = []            # 놓여있는 파이프
cnt = 0             # 잘린 개수
for p in range(len(pipe)):
    if pipe[p] == '(':
        lst.append(p)
    if pipe[p] == ')' and pipe[p-1] == '(':     # 레이저일때
        lst.pop()
        cnt += len(lst)         # 막대기 있는 만큼 잘린개수 세기
    elif pipe[p] == ')':        # 막대기 끝나면 잘린개수 +1
        lst.pop()
        cnt += 1
print(cnt)