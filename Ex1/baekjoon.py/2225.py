N, K = map(int, input().split())

answer = 0
N_list = []
for i in range(1, N+1):
    N_list.append(i)
for j in N_list :
    for l in N_list:
        if j + l == K :
            answer += 1
print(answer % 1000000000)