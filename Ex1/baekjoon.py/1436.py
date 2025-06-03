N = int(input())

f = 666
count = 0
while True :
    if '666' in str(f) :
        count += 1
        if N == count :
            print(f)
            break
    f += 1