import re

# объявим список "game" (он же матрица), в который будем записывать ходы игры
game_ = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# текстовые выводы запишем в переменные, чтобы было удобнее их вызывать в коде
# text_hi = """Выберите символ: 'X' или '0'\n"""
text_var = """Введите координаты в формате "a, b", где a = вертикаль, b - горизонталь. a и b - от 1 до 3.\n"""

# создадим переменную symbol_1, в которую запишем выбор пользователя и приведем его к формату
#   symbol_1 = input(text_hi).upper()

#   if symbol_1 == 'X' or symbol_1 == '0':
#       print('Поздравляю, Вы выбрали ', symbol_1)
#        if symbol_1 == 'X':
#        print('Сопернику достается 0')
#           symbol_2 = '0'
#       else:
#           print('Сопернику достается X')
#           symbol_2 = 'X'
#   else:
#       print(text_hi)

# step_a = re.split(",| |", input(text_var))
# step_b = [i for i in step_a if i]


# def steps():
#    step_a = re.split(",| |", input(text_var))
#    step_b = []
#    for i in step_a:
#        if i:
#            step_b.append(i)
#    return step_b.copy()


# print(step_b)

symbol_1 = 'X'
symbol_2 = '0'

count = 0


def show_game(f):
    print('  1 2 3')
    for i in range(len(game_)):
        print(str(i + 1), *game_[i])


# def check_diagonal_x():  # функция проверки иксов по диагоналям
#     to_right = True
#     to_left = True
#     for i in range(0, 3):
#         to_right &= (game_[i][i] == symbol_1)
#         to_left &= (game_[2 - i][i] == symbol_1)
#     return to_right or to_left


def check_diagonal(symbol):  # функция проверки нолей по диагоналям
    to_right = True
    to_left = True
    for i in range(0, 3):
        to_right &= (game_[i][i] == symbol)
        to_left &= (game_[2 - i][i] == symbol)
    return to_right or to_left


# def check_lines_x():
#     for i in range(0, 3):
#         cols = True
#         rows = True
#         for k in range(0, 3):
#             cols &= (game_[i][k] == symbol_1)
#             rows &= (game_[k][i] == symbol_1)
#         return cols or rows


def check_lines(symbol):
    for i in range(0, 3):
        cols = True
        rows = True
        for k in range(0, 3):
            cols &= (game_[i][k] == symbol)
            rows &= (game_[k][i] == symbol)
        return cols or rows


def users_input(f):
    while True:
        step_a = re.split("[,]| |[.]|", input(text_var))
        step_b = [i for i in step_a if i]
        if len(step_b) != 2:
            print("Введите две координаты.")
            continue
        if not (step_b[0].isdigit() and step_b[1].isdigit()):
            print("Введите числа!")
            continue
        a, b = map(int, step_b)
        if not ((a in range(1, 4)) and (b in range(1, 4))):
            print("Введите координаты от 1 до 3.")
            continue
        x = a - 1
        y = b - 1
        if f[x][y] != '-':
            print("Клетка занята, выберите другую!")
            continue
        break
    return x, y


# def input_symbol()
show_game(game_)


# while (check_diagonal_x() or check_diagonal_0()) or (check_lines_x() or check_lines_0()) is False:
    # Просим ввести координаты и приводим их к нужному виду
    # step_a = re.split("[,]| |[.]|", input(text_var))
    # print(step_a)
    # step_b = [i for i in step_a if i]
    # print(step_b)
    # print(check_diagonal_x(), check_diagonal_0())
    # print(check_lines_x(), check_lines_0())

    # users_input(game_)
    # if game_[int(step_b[0])-1][int(step_b[1])-1] == '-':
    # записываем символы поочередно в матрицу game_
    # if n == 0:
    # game_[int(step_b[0])-1][int(step_b[1])-1] = symbol_1
    # n += 1
    # else:
    # game_[int(step_b[0])-1][int(step_b[1])-1] = symbol_2
    # n -= 1
    # else:
    # print("Клетка занята, выберите другую!")

    #    for i in range(len(game_)):
    #        for j in range(len(game_[i])):
    #            print(game_[i][j], end=' ')
    #        print()
while True:
    x, y = users_input(game_)
    if count % 2 == 0:
        symbol = 'X'
    else:
        symbol = '0'
    game_[x][y] = symbol
    show_game(game_)
    if count == 9:
        print('Ничья!')
        break
    if check_lines(symbol) or check_diagonal(symbol):
        print("Победил ", symbol)
        break
    count += 1

# a = int(step_a[0])
# b = int(step_a[1])
# print(game_[a-1][b-1])
