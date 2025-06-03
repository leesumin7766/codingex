T = int(input())

for test_case in range(1, T+1) :
    S = input().strip()
    
    
    L_list = 0
    R_list = 0
    Q_list = 0
    
    for i in S :
        if i == 'L' :
            L_list += 1
        elif i == 'R' :
            R_list += 1
        elif i == '?' :
            Q_list += 1
    
    if L_list > R_list :
        pos = L_list - R_list 
        print(pos + Q_list)
    elif L_list == R_list :
        pos = R_list - L_list 
        if Q_list == 0 :
            print(L_list + Q_list)
        else :
            print(max(abs(pos + Q_list), abs(pos - Q_list)))
    else :
        pos = R_list - L_list
        print(pos + Q_list) 
    
            