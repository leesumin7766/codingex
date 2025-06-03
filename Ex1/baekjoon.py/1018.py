N, M = map(int, input().split())  # 보드 크기 입력
board = [input().strip() for _ in range(N)]  # 보드 상태 입력

# 체스판 두 가지 패턴 (왼쪽 위가 W 또는 B)
chess1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]
chess2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

def count_recolor(x, y):
    """(x, y)부터 8x8 보드를 확인하고 다시 칠해야 하는 최소 개수 반환"""
    cnt1 = 0  # chess1 패턴과 비교
    cnt2 = 0  # chess2 패턴과 비교
    
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess1[i][j]:  # chess1 패턴과 다르면 +1
                cnt1 += 1
            if board[x + i][y + j] != chess2[i][j]:  # chess2 패턴과 다르면 +1
                cnt2 += 1
                
    return min(cnt1, cnt2)  # 두 패턴 중 최소 수정 개수 반환

# 전체 보드에서 8×8 영역을 확인하며 최소 칠해야 하는 개수를 찾음
min_recolor = float("inf")
for i in range(N - 7):  # N-8+1 개의 행 검사
    for j in range(M - 7):  # M-8+1 개의 열 검사
        min_recolor = min(min_recolor, count_recolor(i, j))

print(min_recolor)