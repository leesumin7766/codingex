import sys
T = int(sys.stdin.readline().strip())

for i in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    print("Case #"+ str(i+1)+ ": "+ str(A)+" + "+ str(B) + " = "+ str(A+B))