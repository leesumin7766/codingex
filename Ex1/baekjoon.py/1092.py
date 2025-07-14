N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort(reversed = True)
M_list.sort(reversed = True)

clear = []
used = []
if max(N_list) < max(M_list) :
    print(-1)
else :
    time = 0
    positions = [0] * N
    checked = [False] * M
    count = 0
    while count < M :
        
        for i in M_list :
            if len(M_list) > 0 :
            for j in N_list :
                if i < j :
                    clear.append(i)
                    used.append(j)
                    M_list.pop()
        else: 
            break
                
if len(M_list) > 0 :
    print(-1)
elif len(N_list) > 0 :
    print(-1)
else :
    print(max(len(used)))