T = int(input())

for t in range(1, T+1):
    word = input()
    sent = input()

    if word in sent:
        print(f'#{t}', "1")
    else:
        print(f'#{t}', "0")