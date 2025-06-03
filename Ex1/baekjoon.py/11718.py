import sys


print(sys.stdin.read()) #   입력받은 모든 내용 그대로 출력


# for line in sys.stdin.readlines():  # 한 줄씩 읽어 리스트로 반환
#     print(line, end='')  # 기본적으로 개행 포함이므로 end=''로 중복 개행 방지