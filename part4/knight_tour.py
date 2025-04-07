import time

knight_moves = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

def is_valid(x, y, board):
    n = len(board)
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def knight_tour_brute(board, x, y, move_count):
    n = len(board)
    if move_count == n * n:
        return True
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            board[nx][ny] = move_count
            if knight_tour_brute(board, nx, ny, move_count + 1):
                return True
            board[nx][ny] = -1
    return False


def count_onward_moves(board, x, y):
    count = 0
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            count += 1
    return count

def knight_tour_heuristic(board, x, y, move_count):
    n = len(board)
    if move_count == n * n:
        return True
    moves = []
    for dx, dy in knight_moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            degree = count_onward_moves(board, nx, ny)
            moves.append((degree, nx, ny))
    moves.sort()
    for _, nx, ny in moves:
        board[nx][ny] = move_count
        if knight_tour_heuristic(board, nx, ny, move_count + 1):
            return True
        board[nx][ny] = -1
    return False

def run_test(n):
    results = {}
    # board = [[-1 for _ in range(n)] for _ in range(n)]
    # board[0][0] = 0
    # start = time.time()
    # knight_tour_brute(board, 0, 0, 1)
    # brute_time = time.time() - start
    # results["brute_time"] = brute_time

    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0
    start = time.time()
    knight_tour_heuristic(board, 0, 0, 1)
    heuristic_time = time.time() - start
    results["heuristic_time"] = heuristic_time

    return results

sizes = [5, 6, 8]
results = {n: run_test(n) for n in sizes}
print(results)
