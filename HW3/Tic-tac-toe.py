from random import randint

class Field:
    def __init__(self):
        # игровое поле
        self.field = [['*', '*', '*'],
                      ['*', '*', '*'],
                      ['*', '*', '*']] 
    
    def print_field(self): # печать игрового поля
        for i in range(len(self.field)): 
            for j in range(len(self.field[i])):
                if j != 2:
                    print(self.field[i][j], end=' ')
                else:
                    print(self.field[i][j], end='\n')
    
    def win(self): # проверка на победу
        for player in ['X', 'O']:
            if (
                # проверка победы в строках
                any(row == [player, player, player] for row in self.field) or
                # проверка победы в столбцах
                any(all(self.field[i][j] == player for i in range(3)) for j in range(3)) or
                # проверка победы в диагоналях
                all(self.field[i][i] == player for i in range(3)) or
                all(self.field[i][2 - i] == player for i in range(3))
            ):
                return player
        return None


class Player:
    def input_coor(self):
        row = int(input('Введите координату по горизонтале: '))
        col = int(input('Введите координату по вертикале: '))
        return row, col


class GameService:
    def drawing_lots(self): # жеребьевка первого хода
        queue = randint(1, 2)
        if queue == 1:
            return 'X'
        else:
            return 'O'
        
    def change_course(self, player): # смена очередности хода
        if player == 'X':
            return 'O'
        else:
            return 'X'

def play():
    print('Игра "Крестики-Нолики"')
    print("Ознакомтесь координатами игрового поля")
    print('  0 1 2\n0 * * *\n1 * * *\n2 * * *')
    f = Field()
    f.print_field()
    g = GameService()
    sign = g.drawing_lots()
    print(f'Первыми ходят {sign}')

    count = 0
    while f.win() is None:
        print(f'Ходят {sign}')
        coor1, coor2 = int(input('Введите координату по горизонтале: ')), int(input('Введите координату по вертикале: '))
        if f.field[coor1][coor2] == '*':
            f.field[coor1][coor2] = sign
            f.print_field()
            count += 1
            sign = g.change_course(sign) # смена знака (хода) X <=> O
            if count == 9:
                print('Ничья')
                break
        else:
            print('Эта клетка уже занята. Попробуйте снова.')

    winner = f.win()
    if winner:
        print(f'Победил игрок {winner}')

if __name__ == '__main__':
    play()