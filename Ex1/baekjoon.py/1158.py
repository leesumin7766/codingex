N, K = map(int, input().split())

N_list = []
for i in range(1, N +1) :
    N_list.append(i)
    
answer = []
start = 0
while N_list :
    start = (start + K - 1) % len(N_list)
    answer.append(N_list.pop(start))

print(f"<{', '.join(map(str, answer))}>")