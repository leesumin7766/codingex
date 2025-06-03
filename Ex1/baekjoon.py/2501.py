N, K = map(int,(input().split()))

nan = []
for i in range(1, N +1) :
    if N % i == 0 :
        nan.append(i)

if len(nan) >= K :
    print(nan[K -1])
else :
    print(0)
