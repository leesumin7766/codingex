N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
A_list = sorted(A)
B_list = sorted(B, reverse = True)

for i in range(N) :
    answer += A_list[i] * B_list[i]
    
print(answer) 