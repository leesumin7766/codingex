import sys

# 입력 받기
N = int(input())  # 수식의 길이
expression = input().strip()  # 수식 문자열

# 숫자와 연산자 분리
numbers = []
operators = []

for i in range(N):
    if i % 2 == 0:
        numbers.append(int(expression[i]))  # 숫자
    else:
        operators.append(expression[i])  # 연산자

# 최댓값 저장 변수
max_result = -float('inf')

# 연산 수행 함수
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

# 백트래킹 (DFS)
def dfs(index, current_value):
    global max_result

    # 수식 끝까지 도달한 경우 최댓값 갱신
    if index == len(operators):
        max_result = max(max_result, current_value)
        return

    # 1. 현재 숫자와 연산
    next_value = calculate(current_value, numbers[index + 1], operators[index])
    dfs(index + 1, next_value)

    # 2. 괄호 사용 (괄호를 추가할 수 있는 경우)
    if index + 1 < len(operators):
        bracket_value = calculate(numbers[index + 1], numbers[index + 2], operators[index + 1])  # 괄호 안 값 계산
        next_value = calculate(current_value, bracket_value, operators[index])  # 현재 값과 괄호 결과 연산
        dfs(index + 2, next_value)  # 두 개 연산을 했으므로 +2

# 초기 DFS 시작 (첫 번째 숫자부터 시작)
dfs(0, numbers[0])

# 결과 출력
print(max_result)
