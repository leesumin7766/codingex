import sys

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(len(A & B))
