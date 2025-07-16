N = int(input())



for _ in range(N) :
    result = list(input())
    stack = 0
    answer = 0
    for i in result :
        
        if i == 'O' :
            stack += 1
            answer += stack
        elif i == 'X' :
            stack = 0
            
    print(answer)