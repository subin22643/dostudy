############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_number = 0
    num_list = list(range(1, number+1))
    numbers = num_list[1:number-1]
    for num in num_list:
        for i in numbers:
            count = 0
            if number % i == 0:
                count += 1

        if count == 0:
            sum_number += num

        return sum_number

    # for i in numbers:
    #     count = 0
    #     if number % i == 0:
    #         count += 1

    # if count == 0:
    #     sum_number += number

    # return sum_number



# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    