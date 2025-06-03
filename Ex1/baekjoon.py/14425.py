N, M = map(int, input().split())

S = {input() for _ in range(N)} # 비교용은 집합 set
SS = [input() for _ in range(M)] # SS는 중복이 있을 수 있으므로 list 사용, set은 중복 제거
answer = 0
for i in SS :
    if i in S :
        answer += 1
print(answer)