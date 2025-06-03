N = set(int(input()) for _ in range(10)) # ==    N = {int(input()) for _ in range(10)}

diff = set((i % 42) for i in N)  # ==    diff = {i % 42 for i in N}
print(len(diff))