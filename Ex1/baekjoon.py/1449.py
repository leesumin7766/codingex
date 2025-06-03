
N, L = map(int, input().split())
N_list = list(map(int, input().split()))
answer = 0
N_list.sort()
    
i = 0
while i < N :
        first = N_list[i]
        answer += 1
        i += 1
        while i < N and N_list[i] <= first + L - 1 :
            i += 1
    
print(answer)
    