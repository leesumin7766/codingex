M = int(input())
N = int(input())

cnt = 0
count = []
for i in range(M, N + 1) :
    if i ** 0.5 % 1 == 0 :
        count.append(i)
        cnt += 1

if cnt > 0 :
            
    print (sum(count))
    print (min(count))
else :
    print(-1)