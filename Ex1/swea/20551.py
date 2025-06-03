T = int(input())

for test_case in range(1, T +1) :
    A, B, C = map(int, input().split())
     
    answer = 0
    new_b = min(B, A + 1)
    new_c = min(C, B + 1)
    
    if A < B and  B < C :
        print(f"#{test_case} 0")
    elif C == 1 :
        print(f"#{test_case} -1")
    elif B <= A or B <= C :
        answer += (B - new_b) + (C - new_c)
        print(f"#{test_case} {answer}")