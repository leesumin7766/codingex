while True :
    T_list = list(map(int, input().split()))

    if T_list[0] == -1 :
        break
    
    answer = 0
    T_list.pop(-1)
    T_list.sort()
    
    for i in T_list :
        if i * 2 in T_list :
            answer += 1
            
    print(answer)