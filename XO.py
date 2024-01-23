def first():
    print('____________________')
    print('| Добро пожаловать |')
    print('|      в игру      | ')
    print('|  крестики-нолики |')
    print('|__________________|')
    print('для начала игры напишите-start')
    print('для того чтобы завершить игру напишите-0')


def show():
    print()
    print("   |  0 |  1  | 2  | ")
    print(' __|____|','____|'*2)
    for i, row in enumerate(field):
        row_str = f" {i} | {'   |  '.join(row)}  |"
        print(row_str)
        print(" __|"'____|','____|'*2)
    print()


def question():
    while True:
        cords = input('    Ваш ход:').split()

        if len(cords) != 2:
            print('Введите координаты!')
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue
        if field[x][y] != "":
            print('Клетка занята!')
            continue
        return x, y
def winner(field):
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),  ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        a, b, c = cord
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != '':
            print(f'Похдравляем! выйграл {field[a[0]][a[1]]}!')
            return True
    return False

first()
info1 = input(":")
field = [[''] * 3 for i in range(3)]
if info1 == 'start':
    print('запуск игры...')

else:
    print('игра завершена')
    quit()
count=0
while True:
    count+=1
    show()

    if count % 2 == 1:
        print('Ходит крестик:')
    else:
        print('Ходит нолик')

    x,y= question()

    if count % 2 == 1:
        field[x][y]= 'X'
    else:
        field[x][y]= 'О'
    if winner(field):
        break
    if count == 9:
        print('Ничья!')
        break
