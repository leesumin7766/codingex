N = int(input())

N_list = []
for _ in range(N) :
    age, name = input().split()
    N_list.append((int(age), name))

N_list.sort(key = lambda x: x[0])

for age, name in N_list :
     print(age, name)