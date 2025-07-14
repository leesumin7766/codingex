S = input()
T = list(input())

while len(S) < len(T) :
    if T[-1] == 'A' :
        T.pop()
    elif T[-1] == 'B' :
        T.pop()
        T.reverse()

T = ''.join(T)
if T == S :
    print(1)
else :
    print(0)

