N = int(input())
M_list = list(map(int, input().split()))

answer = []
for i in range(N) :
    answer.insert(len(answer) - M_list[i], i + 1)

print(answer)