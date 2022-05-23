import re

# объявим список "game" (он же матрица), в который будем записывать ходы игры
game_ = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

text_var = """Введите координаты в формате "a, b", где a = вертикаль, b - горизонталь. a и b - от 1 до 3.\n"""
symbol_1 = 'X'
symbol_2 = '0'
count = 0


# Функция вывода матрицы игры
def show_game(f):
    print('  1 2 3')
    for i in range(len(game_)):
        print(str(i + 1), *game_[i])


# Функция проверки диагоналей
def check_diagonal(symbol):
    to_right = True
    to_left = True
    for i in range(0, 3):
        to_right &= (game_[i][i] == symbol)
        to_left &= (game_[2 - i][i] == symbol)
    return to_right or to_left


# Функция проверки линий
def check_lines(symbol):
    for i in range(0, 3):
        cols = True
        rows = True
        for k in range(0, 3):
            cols &= (game_[i][k] == symbol)
            rows &= (game_[k][i] == symbol)
        return cols or rows


# Функция проверки ввода координат
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


# Начинаем игру
show_game(game_)

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
