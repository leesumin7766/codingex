T = int(input())

for test_case in range(1, T + 1) :
    N = int(input())
    answer = 0
    if N > 2 :
        answer += N // 3
    else :
        pass
    
    print(f"#{test_case} {answer}") 