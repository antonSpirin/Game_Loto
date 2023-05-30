import random
from classes import *

players = []
while True:
    try:
        count_players = int(input('Enter the number of players..'))
    except ValueError:
        print('You did not enter a number, try again')
    else:
        for i in range(count_players):
            print(('-' * 5) + 'Player number ' + str(i + 1) + ('-' * 5))
            while True:
                try:
                    choice_players = input(
                        'Enter \'y\' if the player is a computer or enter \'n\' if the real player... ')
                    if choice_players != 'y' and choice_players != 'n':
                        raise MyExeption('You did not enter \'y\' or \'n\', try again..')
                except MyExeption as e:
                    print(e.data)
                else:
                    if choice_players == 'y':
                        players.append(Player('Computer'))
                        print('Create player - Computer')
                    elif choice_players == 'n':
                        players.append(Player(input('Input you name:')))
                    break

        print('Players:')
        for i in players:
            print(*f'-{i.name}')
        break

# создание игровых карточек
for i in players: i.new_card()
barrels = Barrel()
input("Press Enter to continue...")
print('Player\'s cards:')
for i in players: i.view_card()
# старт игры
print('For get barrel press Enter or exit game press any key.. ')
start = input("Press Enter to continue...")
# count_players = []
barrels.count_barrel = 0

while start == '':
    start = 0
    flag_count_players = False
    # достаем боченки
    barrels.get_number()

    for player in players[::-1]:
        barrels.view_barrel()
        player.view_card()
        # ищем номер боченка на карточке компьютера
        if player.name == 'Computer':
            for i in player.play_card.card_numbers:
                for x in range(len(i)):
                    if barrels.number_barrel == i[x]:
                        i[x] = '\u0336'.join(str(barrels.number_barrel)) + '\u0336'
                        player.count_player += 1
                        print('Result after move:')
                        player.view_card()
        # ищем номер боченка на карточке игрока
        else:
            print('Do you want to cross out a number on your card like on a barrel? ')
            while True:
                try:
                    choice_step = input('If yes, please press \'y\', if no, please press \'n\'')
                    if choice_step != 'y' and choice_step != 'n':
                        raise MyExeption('You did not enter \'y\' or \'n\', try again..')
                except MyExeption as e:
                    print(e.data)
                else:
                    if choice_step == 'y':
                        flag = False  # флаг показывает совпал номер боченка или нет
                        for i in player.play_card.card_numbers:
                            for x in range(len(i)):
                                if barrels.number_barrel == i[x]:
                                    i[x] = '\u0336'.join(str(barrels.number_barrel)) + '\u0336'
                                    player.count_player += 1
                                    print('Result after move:')
                                    player.view_card()
                                    flag = True
                        if not flag:  # если не совпал номер боченка не с одним номером на карточке
                            print('-' * 23)
                            print(f'{player.name} Game over!\n''There is no such number on your card')
                            print('-' * 23)
                            players.remove(player)
                            if len(players) == 1:
                                player = players[0]
                                player.winner()
                                exit()
                    elif choice_step == 'n':
                        for i in player.play_card.card_numbers:
                            for x in range(len(i)):
                                if barrels.number_barrel == i[x]:
                                    i[x] = '\u0336'.join(str(barrels.number_barrel)) + '\u0336'
                                    print('-' * 23)
                                    print(f'{player.name} Game over!\n''There is such number on your card')
                                    print('-' * 23)
                                    players.remove(player)
                                    if len(players) == 1:
                                        player = players[0]
                                        player.winner()
                                        exit()
                    break

    for player in players:
        if player.count_player == 15:
            flag_count_players = True
            player.winner()
            exit()
    if not flag_count_players:  # пока не зачеркнуты все номера на одной из карточек игрока или компьютера
        print('For get barrel press Enter or exit game press any key.. ')
        start = input("Press Enter to continue...")

    barrels.count_barrel += 1  # счетчик боченков









