N = int(input())

N_list = []
for _ in range(N) :
    N_list.append(int(input()))

answer = 0
N_list.sort()
now = []
for i in N_list :
    now.append(i)
    answer += now[-1] + i
    
print(answer - now[-1])