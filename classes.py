# Боченок - 90 штук (с цифрами от 1 до 90).
# Карточка - Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны.
# Игрок - В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.
import random


class Card:
    def __init__(self):
        self.card_numbers = []

    def create_card(self):
        numbers_list = list(range(1, 91))
        card_create = list(random.sample(numbers_list, 15))
        # print(card_create)
        card_str1 = []
        card_str2 = []
        card_str3 = []
        numbers_random_list = []
        for i in range(len(card_create)):
            if i >= 0 and i < 5:
                card_str1.append(card_create[i])
                if i < 4:
                    card_str1.append(' ')
            if i >= 5 and i < 10:
                card_str2.append(card_create[i])
                if i < 9:
                    card_str2.append(' ')
            if i >= 10:
                card_str3.append(card_create[i])
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


class Barrel:
    def __init__(self):
        self.number_barrel = 0
        self.barrels_list = []
        self.count_barrel = 0

    def get_number(self):
        random_number = 0
        while random_number not in self.barrels_list:
            random_number = random.randint(1, 91)
            if random_number not in self.barrels_list:
                self.barrels_list.append(random_number)
                self.number_barrel = random_number
            else:
                random_number = 0

    def view_barrel(self):
        print(f'New barrel number: {self.barrels_list[self.count_barrel]} (left: {89 - self.count_barrel})')


class Player:

    def __init__(self, name):
        self.name = name
        self.play_card = Card()
        self.count_player = 0

    def new_card(self):
        self.play_card.create_card()

    def view_card(self):
        print(f'Player: {self.name}')
        self.play_card.card_print()

    def winner(self):
        print('-' * 23)
        print(f'Congratulation, {self.name}!You win!')
        print('-' * 23)


class MyExeption(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


