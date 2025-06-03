import sys
input = sys.stdin.readline

N = int(input())

N_set = set(input().strip() for _ in range(N))
F_set = set(input().strip() for _ in range(N-1))

answer = []
for i in N_set :
    if i not in F_set :
        answer.append(i)
        
print(answer[0])