def step_player(board, x, y, player):
    player_board = board.copy()
    player_board[x][y] = player
    return player_board

def winner(board):
    winner_player = [((1, 1), (1, 2), (1,3)), \
                     ((2, 1), (2, 2), (2, 3)), \
                     ((3, 1), (3, 2), (3, 3)), \
                     ((1, 1), (2, 1), (3, 1)), \
                     ((1, 2), (2, 2), (3, 2)), \
                     ((1, 3), (2, 3), (3, 3)), \
                     ((1, 1), (2, 2), (3, 3)), \
                     ((1, 3), (2, 2), (3, 1))]
    for win in winner_player:
        symbols = []
        for i in win:
            symbols.append(board[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            print(("Win X!!!"))
            return False
        if symbols == ["O", "O", "O"]:
            print("Win O!!!")
            return False
    return True

def input_cordinate():
    i_go_it = True
    player1 = 'X'
    temp_player = ''
    player2 = 'O'
    count = 1
    while i_go_it:
        try:
            x, y = input("Введите две координаты ").split()
        except ValueError:
            continue
        if not x.isdigit() or not y.isdigit():
            print("Введите цифры ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Вне диапазона. Попробуйте еще ")
            continue
        if 'X' in board[x + 1][y + 1] or \
                'O' in board[x + 1][y + 1]:
            print("Введите заново корординаты")
            continue
        else:
            for i in (step_player(board, x + 1, y + 1, player1)):
                print(*i)
        i_go_it = winner(board)
        if i_go_it:
            if count == 9:
                print("Ничья")
                i_go_it = False
        count += 1
        temp_player = player1
        player1 = player2
        player2 = temp_player

board = [[' ', '0', '1', '2'],\
         ['0', '-', '-', '-'],\
         ['1', '-', '-', '-'],\
         ['2', '-', '-', '-']]
print("""Добро пожаловать в игру крестики-нолики
----------------------------------------
Для начала игры пусть 1 игрок введет 
координаты X = от 0 до 2 и Y = от 0 до 2
--------------------------------------
Приятного вам время препровождения""")
for i in board:
    print(*i)

while True:
    g = input("Вы хотите играть Yes или No?")
    if g == "Yes":
        for i in board:
            print(*i)
        input_cordinate()
    elif g == "No":
        print("Хорошего вам дня!!!")
        break
    else:
        continue



