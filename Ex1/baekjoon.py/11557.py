T = int(input())

for testcase in range(T) :
    N = int(input())
    max_L = 0
    max_S = ''
    for _ in range(N) :
        S, L = input().split()
        L = int(L)
        if L > max_L :
            max_L = L
            max_S = S

    print(max_S)
    