X = int(input())
N = int(input())
T = 0
for _ in range(N) :
    a, b = map(int, input().split())
    T += a * b
if T == X :
    print("Yes")
else :
    print("No")