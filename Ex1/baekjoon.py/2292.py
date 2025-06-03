# 1 6 12 18 24 30 36
N = int(input())

if N == 1 :
    print(1)
else :
    answer = 1
    cnt = 1
    while cnt < N :
        cnt += 6 * answer
        answer += 1
    
    print(answer)