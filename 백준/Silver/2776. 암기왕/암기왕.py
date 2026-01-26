T = int(input())

for _ in range(T) :

    N = int(input())
    N_1 = set(map(int, input().split()))

    N_2 = int(input())
    N_list = []
    N_list += list(map(int, input().split()))

    for i in N_list :
        if i in N_1 :
            print(1)
        else :
            print(0)