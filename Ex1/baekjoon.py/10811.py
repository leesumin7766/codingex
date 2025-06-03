N, M = map(int, input().split())

baskets = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets) # 3 4 1 2 5  *(언패킹 연산자) 리스트의 각 요소를 공백으로 구분하여 출력
print(baskets)  #[3, 4, 1, 2, 5] 리스트 형식 그대로, []와 , 포함