import sys
input = sys.stdin.readline

N = int(input())

h_list = [int(input()) for _ in range(N)]
max_h = h_list[-1]
answer = 1

for i in range(N -2, -1, -1) :
    if h_list[i] > max_h :
          answer += 1
          max_h = h_list[i]

print(answer)