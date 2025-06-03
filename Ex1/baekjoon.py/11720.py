N = int(input())
N_list = input()
answer = 0
for i in range(N) :
    answer += int(N_list[i])

print(answer)

# for i in range(N):는 N번 반복하는 경우 사용되며, i는 0부터 N-1까지의 숫자를 차례대로 가집니다.
# 예: range(5)는 0, 1, 2, 3, 4의 값만 반복합니다.
# for i in N:는 N이 리스트나 튜플 등의 반복 가능한 객체일 경우, 그 객체의 각 요소를 하나씩 반복합니다.
# 예: N = [1, 2, 3, 4, 5]일 경우, 1, 2, 3, 4, 5를 차례대로 i에 할당하여 반복합니다.
