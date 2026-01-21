from itertools import permutations

N, M = map(int, input().split())

N_list = list(range(1, N + 1))

for p in permutations(N_list, M) :
    print(*p)