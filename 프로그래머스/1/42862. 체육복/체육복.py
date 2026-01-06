def solution(n, lost, reserve):
    # 여벌 체육복이 있지만 도난당한 학생 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
        else:
            continue

        lost_set.remove(student)

    return n - len(lost_set)
