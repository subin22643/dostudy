T = int(input())

for t in range(1, T+1):
    word = input()
    n = len(word)

    count = 0
    for i in range(n//2):
        if word[i] == word[n-1-i]:
            count += 1
        else:
            break
    if count == n//2:
        print(f'#{t}', "1")
    else:
        print(f'#{t}', "0")