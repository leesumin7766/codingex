N = int(input())

N_list = []
answer = 0
for _ in range(N) :
    N_list += [int(input())]

N_list.sort()

for i in range(N) :
    weight = N_list[i] * (N-i)
    answer = max(answer, weight)

print(answer)