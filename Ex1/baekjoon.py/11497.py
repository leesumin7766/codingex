from collections import deque

T = int(input())

for test_case in range(1, T+1) :
    N = int(input())
    L = list(map(int, input().split()))
    
    L_deque = deque()
    
    L.sort()
    for i in range(N) :
        if i % 2 != 0 :
            L_deque.append(L[i])
        elif i % 2 == 0 :
            L_deque.appendleft(L[i])
    max_height = 0
    for i in range(N) :
        height = abs(L_deque[i] - L_deque[(i + 1) % N])
        max_height = max(max_height,height)
    
    print(max_height)

