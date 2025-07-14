n_list = [int(input()) for _ in range(10)]

answer = 0

for i in n_list :
    answer += i
    if answer >= 100 :
        if answer - 100 <= 100 - (answer - i) :
            print(answer)
        else :
            print(answer - i)
        break
    
else :
    print(answer)