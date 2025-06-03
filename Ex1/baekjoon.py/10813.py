# # 입력 받기
# N, M = map(int, input().split())

# # 바구니 초기화: 1번부터 N번까지 해당 번호의 공을 넣음
# baskets = [i for i in range(1, N + 1)]

# # M번 공을 교환
# for _ in range(M):
#     i, j = map(int, input().split())
#     # 두 바구니의 공을 교환 (swap)
#     baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

# # 결과 출력
# print(*baskets)
    
        
    