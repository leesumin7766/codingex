N, M = map(int, input().split())


if N == 1 :
    print(1) 
elif N == 2 :
    for i in range(1, M, 2) :
        answer = 0
        answer += 1
        print(answer)
else :
    if M < 7 :
        print(min(4, M))
    else :
        print(M-2)