N = int(input())
N_list = []
for _ in range(N) :
    N_list.append(int(input()))

N_list.sort()

print(N_list[0] * N)