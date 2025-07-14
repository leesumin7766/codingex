from collections import Counter

n = int(input())
k = int(input())

n_list = []
for _ in range(n):
    n_list = int(input())
    
answer = []
for i in n_list :
    answer.append(i)
    
print(Counter(answer))