N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N) :
    result = [A[i][j] + B[i][j] for j in range(M)]
    print(*result) #    * 는 리스트 형태 출력에서 -> 공백으로 출력