import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

N_list = set(input().strip() for _ in range(N)) 
M_list = list(input().strip() for _ in range(M))

for i in M_list :
    if i in N_list :
        answer.append(i)    
        
answer.sort()

print(len(answer))
for i in answer :
    print(i)