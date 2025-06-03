A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

A_count = A_set - B_set
B_count = B_set - A_set

print(len(A_count) + len(B_count))