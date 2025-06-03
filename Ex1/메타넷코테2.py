def solution(names, homes, grades):
    students = [] # 각 학생의 정보를 저장할 리스트
    
    for i in range(len(names)):
        name = names[i]
        home = homes[i]
        grade = grades[i]

        front_digit = int(str(grade)[0]) # 성적의 첫 번째 자릿수 추출(일의 자리만 구분)
        x, y = home[0], home[1]          # 집의 x, y 좌표 추출
        distance = x**2 + y**2           # 집의 좌표를 기준으로 원점에서의 거리 계산
        students.append((name, front_digit, distance, grade, i))  # 학생 정보를 튜플로 저장
    
    students.sort(key=lambda x: (-x[1], -x[2], x[0])) #students 리스트를 특정 정렬 기준에 따라 정렬하는 부분, 
                                                      # sort 함수 = 리스트 정렬 함수(nlog n) / 
                                                      # 정렬 기준 = lambda : 익명 함수(이름이 없는 함수)를 만드는 데 사용
                                                      #-x[1]: 첫 번째 자릿수 기준 내림차순 (높은 성적을 우선).
                                                      #-x[2]: 거리가 먼 순서로 내림차순 (원점에서 멀리 사는 학생을 우선).
                                                      # x[0]: 이름 기준 오름차순 (동일 조건일 경우, 알파벳 순서로 정렬).
    
    rankings = [0] * len(names) #각 학생의 순위를 저장할 리스트로 초기화.
    for rank, student in enumerate(students, 1): # 정렬된 students 리스트를 순회하며 순위를 부여합니다.
                                                 # 각 학생의 인덱스(student[4])를 기반으로 rankings 리스트의 해당 위치에 순위를 저장합니다.
        rankings[student[4]] = rank
    return rankings