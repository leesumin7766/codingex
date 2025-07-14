N, M = map(int, input().split())

str_N = {}
int_N = {}

for i in range(1 , N + 1) :
    name = input().strip()
    str_N[name] = i
    int_N[str(i)] = name

for _ in range(M) :
    M_list = input().strip()
    if M_list.isdigit() :
        print(int_N[M_list])
    else :
        print(str_N[M_list])