A = set(range(1, 31)) # set 집합으로 1 - 30까지 받기

S = set(int(input()) for _ in range(28)) #제출한 input() 28명 받기

N = sorted(A - S) # A - S를 sorted 정렬(작은 순)
print(N[0])
print(N[1])