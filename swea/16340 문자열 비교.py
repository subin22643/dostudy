T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{t}', "1")
    else:
        print(f'#{t}', "0")

# 삼항조건 연산자 사용
    # result = 1 if str1 in str2 else 0
    # print(f'#{t} {result}')