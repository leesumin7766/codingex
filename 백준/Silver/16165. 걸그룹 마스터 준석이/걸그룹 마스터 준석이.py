N, M = map(int, input().split())

team_to_members = {}
member_to_team = {}

for _ in range(N) :
    team_name = input()
    member_cnt = int(input())
    members = []
    for _ in range(member_cnt) :
        member = input().strip()
        members.append(member)
        member_to_team[member] = team_name

    members.sort()
    team_to_members[team_name] = sorted(members)


for _ in range(M) :
    quiz_name = input().strip()
    quiz = int(input())
    if quiz == 0 :
        for m in team_to_members[quiz_name] :
            print(m)
    else :
        print(member_to_team[quiz_name])