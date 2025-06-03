def solution() :    
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()
    
    answer = 0
    sum_answer = 0
    for i in P :
        answer += i
        sum_answer += answer
    
    return sum_answer
print(solution())