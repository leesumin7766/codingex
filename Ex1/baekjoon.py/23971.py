# H, W, N, M = map(int, input().split())

# count = 0
# for i in range(1,H+ 1, N+1):
#     for j in range(1, W+ 1, M+1) :
#         count += 1

# print(count)

H, W, N, M = map(int, input().split())

rows = (H - 1) // (N + 1) + 1
cols = (W - 1) // (M + 1) + 1

print(rows * cols)