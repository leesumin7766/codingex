N = int(input())
K = int(input())

answer = 0
distance = []
N_list = list(map(int, input().split()))

N_list.sort()

for i in N_list :
    distance = i - (i-1)
  
print(distance)  