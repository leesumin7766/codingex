N = int(input())

answer = 0
meet = set()
meet.add("ChongChong")

for _ in range(N) :
    A, B = input().split()

    if A in meet or B in meet :
        meet.add(A)
        meet.add(B)

print(len(meet))