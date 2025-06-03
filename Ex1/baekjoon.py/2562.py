N = [int(input()) for _ in range(9)]

max_n = max(N)
maxwhere = N.index(max_n) + 1

print(max_n)
print(maxwhere)