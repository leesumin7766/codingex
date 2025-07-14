N = int(input())
gap = list(map(int, input().split()))
N_list = list(map(int, input().split()))

answer = 0
filled = N_list[0]
for i in range(N-1) :
    if N_list[i] < filled :
        filled = N_list[i]
    answer += filled * gap[i]

print(answer)