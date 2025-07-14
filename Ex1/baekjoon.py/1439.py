S = input()

count_zero = 0
count_one = 0
first = S[0]
if first == '1' :
    count_one += 1
if first == '0' :
    count_zero += 1
    
for i in S :
    if i == first :
        pass
    elif i != first :
        if i == '1' :
            count_one += 1
            first = i
        elif i == '0' :
            count_zero += 1
            first = i

print(min(count_zero, count_one))    