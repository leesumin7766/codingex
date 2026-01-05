def solution(s):
    answer = 0
    x = None
    x_count = 0
    no_x = 0
    for i in s :
        if x is None :
            x = i
            
        if i == x :
            x_count += 1
        else :
            no_x += 1
            
        if x_count == no_x:
            answer += 1
            x = None
            x_count = 0
            no_x = 0
            
    if x is not None:
        answer += 1
        
    return answer