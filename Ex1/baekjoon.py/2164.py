# list <-- 시간초과
# N = int(input())

# answer = 0

# N_list = list(range(1, N + 1))

# while len(N_list) > 1 :
#     N_list.pop(0)
#     N_list.append(N_list.pop(0))

# print(*N_list)
from collections import deque

N = int(input())
N_deque = deque(range(1, N + 1))

while len(N_deque) > 1 :
    N_deque.popleft()
    N_deque.append(N_deque.popleft())    

print(*N_deque)