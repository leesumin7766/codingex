T = int(input())

for test_case in range(1, T + 1) :
    N = int(input())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = []
        
    for j in range(N) :
        if A[j] <= B[j] :
            answer.append("A")
        else :
            answer.append("B")
        

    print("".join(answer))