N = int(input())

NN = [int(input()) for _ in range(N)]
NN.sort()
for i in NN :
    print(i)
    
# N = int(input())
# NN = (int(input()) for _ in range(N))  # 제너레이터 그대로 사용
# for i in sorted(NN):  # 정렬된 결과를 바로 순회
#     print(i)