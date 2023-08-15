T = int(input())

for t in range(1, T+1):
    text = input()
    stack = []

# 괄호검사 (올바른 괄호사용인지)
    for i in text:
        if i in '(){}':
            stack.append(i)
        if len(stack) > 1:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
            elif stack[-1] == '}' and stack[-2] == '{':
                stack.pop()
                stack.pop()
    num = 0
    lst = []
    if stack == []:     # 괄호의 짝이 맞으면 실행
        if text[0] != '(' and text[0] != '{':           # 첫 숫자가 괄호에 둘러 쌓이지 않는 경우 -1 출력
            print(f'#{t} -1')
        elif text[-1] != ')' and text[-1] != '}':       # 마지막 숫자가 괄호에 둘러 쌓이지 않는 경우 -1 출력
            print(f'#{t} -1')
        else:                                           # 숫자들이 괄호에 둘러쌓여 있다면 실행
            for j in range(len(text)):
                lst.append(text[j])                     # 빈 리스트에 모든 문자를 하나씩 append
                if text[j] == ')':                      # 소괄호가 끝나면
                    lst.pop()                           # 닫는 괄호를 lst에서 빼고
                    while lst[-1] != '(':               # 여는 괄호가 나오기 전까지
                        num += int(lst.pop())           # 소괄호 안의 숫자들을 더하기
                    lst.pop()                           # 여는 괄호가 나오면 while문 종료, 여는 괄호 삭제
                elif text[j] == '}':                    # 같은 방법으로 중괄호가 나오면
                    lst.pop()
                    while lst[-1] != '{':
                        if num == 0:                    # 아무 수도 더해지지 않은 채 중괄호{}가 나오면
                            num = int(lst.pop())        # num이 0이므로 아무리 곱해도 0이 나오게 됨. num을 중괄호 안의 숫자로 바꾸기
                        else:
                            num = num * int(lst.pop())  # 중괄호 안의 숫자들을 곱하기
                    lst.pop()
            print(f'#{t} {num}')
    else:   # 괄호의 짝이 맞지 않는 경우 -1 출력
        print(f'#{t} -1')