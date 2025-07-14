X = int(input())

line = 1
up = 1
down = 1
answer = 1
while answer < X :
    X -= line
    line += 1

if line % 2 == 0 :
    