import sys

input = sys.stdin.readline

N = int(input())
N_list = []
for _ in range(N) :
    N_list.append(int(input()))

N_list.sort()
for i in N_list:
    
    print(i)