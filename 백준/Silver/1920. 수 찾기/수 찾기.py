N = int(input())

A_list = set(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))

for i in M_list :
    if i in A_list :
        print(1)
    else :
        print(0)