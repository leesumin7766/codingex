T = int(input())

for _ in range(T) :
    left = []
    right = []
    testcase = input()
    for i in testcase :
        if i == '<' :
            if left :
                right.append(left.pop())
        elif i == '>' :
            if right :
                left.append(right.pop())
        elif i == '-' :
            if left :
                left.pop()
        else :
            left.append(i)
    right = list(reversed(right)) # reversed 하면 리스트에서 이터레이터로 변경되므로 다시 리스트로 설정
    print(''.join(left + right))