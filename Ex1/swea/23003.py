T = int(input())

for test_case in range(1, T + 1) :
    S, P = map(str, input().split())
    
    T_list = ["red", "orange", "yellow", "green", "blue", "purple"]
    S_index = T_list.index(S)
    P_index = T_list.index(P)
    
    if S == P :
        print("E")
    elif (S_index -1) % 6 == P_index or (S_index +1) % 6 == P_index :
        print("A")
    elif (S_index +3) % 6  == P_index :
        print("C")
    else :
        print("X")