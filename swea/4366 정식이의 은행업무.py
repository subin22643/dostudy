T = int(input())
for t in range(1, T+1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    bi_dec = []
    result = 0

   # 2진수를 10진수로 변환
    for i in range(len(binary)):
       binary[i] = (binary[i]+1) % 2        # 어떤 수가 틀렸는지 하나씩 바꾸기
       num2 = 0
       for j in range(len(binary)):
           num2 += 2**j * binary[-(j+1)]
       bi_dec.append(num2)
       binary[i] = (binary[i] + 1) % 2      # 원래대로 복구


    # 3진수를 10진수로 변환하여 2진수 변환 숫자랑 비교
    for i in range(len(trinary)):
        for _ in range(2):
            trinary[i] = (trinary[i]+1) % 3
            num3 = 0
            for j in range(len(trinary)):
                num3 += 3**j * (trinary[-(j+1)])
            if num3 in bi_dec:
                result = num3
                break

        trinary[i] = (trinary[i] + 1) % 3

    print(f'#{t}',result)