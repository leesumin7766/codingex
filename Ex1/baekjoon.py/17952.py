N = int(input())

answer = 0
remain = []

for _ in range(N) :
    doing = input().split()
    if doing[0] == '1' :
        A = int(doing[1])
        T = int(doing[2])
        remain.append([A, T])
    
    if remain :
        remain[-1][1] -= 1
        if remain[-1][1] == 0 :
            answer += remain[-1][0]
            remain.pop()

print(answer)
        