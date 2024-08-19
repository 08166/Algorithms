def solve_n_queen(board, col, n):
    # 모든 열에 퀸을 배치한 경우 (기저 사례)
    if col >= n:
        return True  # 성공적으로 모든 퀸을 배치한 경우 True 반환

    # 현재 열(col)에 퀸을 배치할 수 있는 모든 행(row)을 확인
    for i in range(n):
        if is_safe(board, i, col, n):  # 현재 위치에 퀸을 배치해도 안전한지 확인
            board[i][col] = 1  # 현재 위치에 퀸을 배치

            # 다음 열에 퀸을 배치하기 위해 재귀적으로 함수 호출
            if solve_n_queen(board, col + 1, n):
                return True  # 다음 열에 퀸을 배치하는 데 성공한 경우 True 반환

            # 만약 다음 열에 퀸을 배치하는 데 실패한 경우, 현재 배치를 취소하고 다른 행을 시도
            board[i][col] = 0  # 백트래킹: 퀸을 다시 제거

    # 현재 열에 퀸을 배치할 수 없으면 False 반환
    return False


def is_safe(board, row, col, n):
    # 현재 행의 왼쪽에 퀸이 있는지 확인
    for i in range(col):
        if board[row][i] == 1:
            return False  # 퀸이 있으면 안전하지 않으므로 False 반환

    # 왼쪽 위 대각선에 퀸이 있는지 확인
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False  # 퀸이 있으면 안전하지 않으므로 False 반환
        i -= 1
        j -= 1

    # 왼쪽 아래 대각선에 퀸이 있는지 확인
    i, j = row, col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False  # 퀸이 있으면 안전하지 않으므로 False 반환
        i += 1
        j -= 1

    # 현재 위치에 퀸을 배치해도 안전한 경우 True 반환
    return True


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))  # 각 위치의 값을 출력
    print()  # 행의 끝에서 줄바꿈


def main():
    n = 4  # 체스판의 크기 (n x n)
    board = [[0] * n for _ in range(n)]  # 체스판을 나타내는 2차원 배열, 0은 퀸이 없음을 의미하고 1은 퀸이 있음을 의미
    if solve_n_queen(board, 0, n):  # NQueen 문제를 해결하는 함수 호출, 성공 시 체스판 출력
        print_board(board)
    else:
        print("Solution does not exist")  # 해결책이 없을 경우 출력


if __name__ == "__main__":
    main()