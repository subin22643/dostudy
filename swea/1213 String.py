for _ in range(10):
    t = int(input())
    word = input()
    sent = input()

    count = 0
    for i in range(len(sent)-len(word) + 1):
        if sent[i:i+len(word)] == word:
            count += 1
    print(f'#{t}', count)