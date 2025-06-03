import bisect

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()
answer = []
for i in M_list :
    left = bisect.bisect_left(N_list, i)
    right = bisect.bisect_right(N_list, i)
    answer.append(str(right - left))

print(' '.join(answer))
