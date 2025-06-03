string = input()
answer = 0
for i in string :
    if i in ['A' , 'B' ,'C'] :
        answer += 3
    elif i in ['D' , 'E' ,'F']:
        answer += 4
    elif i in ['G' , 'H' ,'I'] :
        answer += 5
    elif i in ['J' , 'K' ,'L'] :
        answer += 6
    elif i in ['M' , 'N' ,'O'] :
        answer += 7
    elif i in ['P' , 'Q' ,'R', 'S'] :
        answer += 8
    elif i in ['T' , 'U' ,'V'] :
        answer += 9
    else :
        answer += 10
        
print(answer)