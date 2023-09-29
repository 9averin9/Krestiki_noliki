def print_board(board):  #Рисуем доску
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):  #Функция проверки победителя
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):  #Фунцкия заполненой доски
    return all(cell != " " for row in board for cell in row)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Добро пожаловать в игру Крестики-Нолики!")

    while not winner and not is_full(board):
        print_board(board) #Вывод изначальной доски
        print(f"Ход игрока {current_player}")

        row = int(input("Выберите строку (0, 1, 2): "))
        col = int(input("Выберите столбец (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ": #Проверяем корректность хода
            print("Недопустимый ход. Попробуйте еще раз.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            winner = current_player
        else:
            current_player = "O" if current_player == "X" else "X"

    print_board(board) #Вывод доски после хода

    if winner:
        print(f"Победил игрок {winner}!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    main()
