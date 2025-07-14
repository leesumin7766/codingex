N = int(input())

class_time = [tuple(map(int, input().split())) for _ in range(N)]
answer = 1
end_class = []

class_time.sort(key = lambda x: (x[1], x[0]))
for S,T in class_time :
    end_class.sort()
    if S < end_class[0] :
        answer += 1
    else :
        for i in end_class :
            if T >= i :
                end_class = T
                pass
        
print(answer)