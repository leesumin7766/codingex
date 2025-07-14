N = int(input())

N_list = list(map(int, input().split()))
K = int(input())

def tastes(N, N_list, K) :
    group_size = 1
    while N // group_size != K :
        group_size *= 2
    
    result = []
        