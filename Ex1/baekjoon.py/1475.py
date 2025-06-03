N = int(input())

N = str(N)

answer = 1
iset = []
for i in N :
    iset.append(i)
    if i in iset :
          answer += 1
          
