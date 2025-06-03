X, Y = map(int, input().split())

Z = int(Y * 100 / X)

if Z >= 99 :
    print(-1)
else :
    left = 1
    right = 10 ** 9
    answer = -1
    
    while left <= right :
        mid = (left + right) // 2
        Z_up = int((Y + mid) * 100 / (X + mid))
        
        if Z_up > Z :
            answer = mid
            right = mid -1
        else :
            left = mid + 1
            
    print(answer) 