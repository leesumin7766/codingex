N, M = int(input().split())

M_list = []
for i in range(M) :
    M_list.append(i)

answer = 0
remained = 0
max_list = 0

left = N - remained
max_M = max(M_list)
M_list.sort()

for j in M_list :
    if j == max_M :
        max_list += 1
        M_list.pop()
    else :
        remained += 1
        
max_M2 = max(M_list)        

if len(max_list) > left :
    

else :
    