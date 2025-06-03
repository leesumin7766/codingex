N = int(input())

for i in range(1, N +1) :
    print(" " * (N -i) + "*" * (i) + "*" * (i- 1))
for k in range(N, 1, -1) :
    print(" " * ((N+ 1) - k) + "*" * (k-1) + "*" * (k-2))
    