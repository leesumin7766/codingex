N = [list(map(int, input().split())) for _ in range(9)]

max_n = -1
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if N[i][j] > max_n:
            max_n = N[i][j]
            row, col = i + 1, j + 1
            
print(max_n)
print(row, col)