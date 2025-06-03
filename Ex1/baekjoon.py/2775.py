T = int(input())

for _ in range(1,T+1) :
    k = int(input())
    n = int(input())

answer = 0
for i in range(k+1) :
    for j in range(1, n + 1) :
        answer += 1
print(answer)