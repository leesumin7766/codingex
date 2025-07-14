N = int(input())

S_list = []
for _ in range(N) :
    name, K, E, M = input().split()
    S_list.append((name, int(K), int(E), int(M)))
    
S_list.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in S_list :
    print(i[0])