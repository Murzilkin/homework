# Создаем пустое поле 3x3
board = [['-' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(board[i][j], end=' ')
        print()

def check_winner(board, player):
    # Проверяем строки и столбцы
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Проверяем диагонали
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

def tic_tac_toe():
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input("Выберите строку (0, 1, 2): "))
            col = int(input("Выберите столбец (0, 1, 2): "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число от 0 до 2.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Некорректный ввод. Строка и столбец должны быть в диапазоне от 0 до 2.")
            continue

        if board[row][col] != '-':
            print("Эта клетка уже занята, выберите другую.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        elif is_board_full(board):
            print_board(board)
            print("Ничья!")
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
