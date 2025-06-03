N = []
for _ in range(9) :
    N.append(int(input()))

total = sum(N)

found = False
for i in range(9) :
    for j in range(i +1, 9) :
        if  total - (N[i] + N[j]) == 100 :
            del1 = N[i]
            del2 = N[j]
            found = True
            break
    if found :
        break

N.remove(del1)
N.remove(del2)
N.sort()
for s in N :
    print(s)