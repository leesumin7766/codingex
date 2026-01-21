N = int(input())

N_list = list(map(int, input().split()))
answer = []
for i in range(1, N + 1) :
    if i == 1 :
        answer.append(i)
    else :
        location = N_list[i -1]
        answer.insert(len(answer) - location, i)

print(*answer)