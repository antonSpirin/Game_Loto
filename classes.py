# Боченок - 90 штук (с цифрами от 1 до 90).
# Карточка - Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны.
# Игрок - В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.
import random
import math


class Card:
    def __init__(self):
        self.card_numbers = []  # готовая карточка игрока с пробелами
        self.card_create = []  # список рандомных чисел для форморования картошки игрока

    def create_card(self):
        numbers_list = list(range(1, 91))
        self.card_create = list(random.sample(numbers_list, 15))
        # print(card_create)
        card_str1 = []
        card_str2 = []
        card_str3 = []
        numbers_random_list = []
        for i in range(len(self.card_create)):
            if i >= 0 and i < 5:
                card_str1.append(self.card_create[i])
                if i < 4:
                    card_str1.append(' ')
            if i >= 5 and i < 10:
                card_str2.append(self.card_create[i])
                if i < 9:
                    card_str2.append(' ')
            if i >= 10:
                card_str3.append(self.card_create[i])
                if i < 14:
                    card_str3.append(' ')
        random.shuffle(card_str1)
        random.shuffle(card_str2)
        random.shuffle(card_str3)
        numbers_random_list.append(card_str1)
        numbers_random_list.append(card_str2)
        numbers_random_list.append(card_str3)
        self.card_numbers = numbers_random_list
    def card_print(self):
        print('-' * 23)
        for i in self.card_numbers:
            print(*i)
        print('-' * 23)

    def __str__(self):
        return f'Список чисел для формирования карточки игрока: {self.card_create}'

    def __eq__(self, other):
        return len(self.card_numbers) == len(other.card_numbers)

    def __ne__(self, other):
        return self.card_numbers != other.card_numbers


class Barrel:
    def __init__(self):
        self.number_barrel = 0
        self.barrels_list = []
        self.count_barrel = 0  # счетчик показывает сколько боченков мы взяли
        self.left_barrels = 90

    def get_number(self):
        random_number = 0
        while random_number not in self.barrels_list:
            random_number = random.randint(1, 90)
            if random_number not in self.barrels_list:
                self.barrels_list.append(random_number)
                self.number_barrel = random_number
            else:
                random_number = 0
        self.count_barrel += 1
        self.left_barrels -= 1

    def view_barrel(self):
        print(f'New barrel number: {self.number_barrel} (left: {self.left_barrels})')

    def __str__(self):
        return (f'New barrel number: {self.number_barrel} (left: {self.left_barrels})')

    def __eq__(self, other):
        return len(self.barrels_list) == len(other.barrels_list)

    def __ne__(self, other):
        return self.number_barrel != other.number_barrel

    def __call__(self, *args, **kwargs):
        return self.number_barrel


class Player:
    def __init__(self, name):
        self.name = name
        self.play_card = Card()
        self.count_player = 0  # счетчик зачеркнутых номеров на карточке игрока

    def new_card(self):
        self.play_card.create_card()

    def view_card(self):
        print(f'Player: {self.name}')
        self.play_card.card_print()

    def winner(self):
        print('-' * 23)
        print(f'Congratulation, {self.name}!You win!')
        print('-' * 23)

    def __str__(self):
        return f'Name player: {self.name} {self.play_card.card_print()}'

    def __eq__(self, other):
        return self.play_card == other.play_card  # так будет работать, потому что это обьект класса Card и тем уже определен метод сравнения

    def __ne__(self, other):
        return self.name != other.name






class MyExeption(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


if __name__ == '__main__':
    pass
