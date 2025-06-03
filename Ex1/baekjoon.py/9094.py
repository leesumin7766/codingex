import sys

T = int(sys.stdin.readline())

cache = dict()

for _ in range(T) :
    n, m = map(int, input().split())
    if (n,m) in cache :
        print(cache[(n,m)])
        continue
    
    count = 0
    
    for a in range(1, n) :
        for b in range(a+1, n) :
            if (a*a + b*b + m) % (a*b) == 0:
                count += 1
    cache[(n,m)] = count
    print(count)
