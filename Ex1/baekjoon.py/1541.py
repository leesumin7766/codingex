S = input()

part = S.split('-')
remain = 0

for i in part[1:] :
    remain += sum(map(int, i.split('+')))
    
print(sum(map(int, part[0].split('+'))) - remain)