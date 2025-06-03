N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = ''
for i in range(N) :
    if A[i] < X:
        answer += str(A[i]) + " "
print(answer)

# 리스트로 저장할 경우
answer = []
for i in range(N):
    if A[i] < X:  # 리스트 요소가 X보다 작은 경우
        answer.append(A[i])

print(*answer)  # 리스트를 공백으로 구분하여 출력