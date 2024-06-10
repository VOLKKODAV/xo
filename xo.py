def check_winner():
    if area[0][0] == 'x' and area[0][1] == 'x' and area[0][2] == 'x':
        return 'x'
    if area[1][0] == 'x' and area[1][1] == 'x' and area[1][2] == 'x':
        return 'x'
    if area[2][0] == 'x' and area[2][1] == 'x' and area[2][2] == 'x':
        return 'x'
    if area[0][0] == 'x' and area[1][0] == 'x' and area[2][0] == 'x':
        return 'x'
    if area[0][1] == 'x' and area[1][1] == 'x' and area[2][1] == 'x':
        return 'x'
    if area[0][2] == 'x' and area[1][2] == 'x' and area[2][2] == 'x':
        return 'x'
    if area[0][0] == 'x' and area[1][1] == 'x' and area[2][2] == 'x':
        return 'x'
    if area[0][2] == 'x' and area[1][1] == 'x' and area[2][0] == 'x':
        return 'x'
    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':
        return '0'


def draw_area():
    for i in area:
        print(*i)

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Вечер в хату')
print('--------------')
draw_area()
for turn in range(1, 10):
    print(f'ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('ходят нолики')
    else:
        turn_char = 'x'
        print('ходют крестики')
    row = int(input('чирканм циферку строчки (1, 2, 3):')) -1
    col = int(input('чиркани циферку столбика (1, 2, 3):')) -1
    if area[row][col] == '*':
        area[row][col] = turn_char
    else:
        print('занято, ступай дальше')
        continue

    draw_area()
    if check_winner() == 'x':
        print('победа туза крестового!')
        break
    if check_winner() == '0':
        print('победа нулика!')
        break
    if check_winner() == '*' and turn == 9:
        print("победила дружба")
