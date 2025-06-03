N = int(input())
n_list = set((map(int,input().split())))
M = int(input())
m_list = list((map(int,input().split())))
answer = []
for i in m_list :
    if i in n_list :
        answer.append(1)
    else :
        answer.append(0)
print(*answer)