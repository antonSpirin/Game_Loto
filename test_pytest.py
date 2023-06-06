from classes import Card, Barrel, Player


class TestCard:
    def test_card_numbers(self):
        card_player = Card()
        card_player.create_card()
        assert len(card_player.card_create) == 15

    def test_number_in_range(self):
        card_player = Card()
        card_player.create_card()
        assert all(ele >= 1 and ele < 91 for ele in card_player.card_create) == True

    def test_eq(self):
        card1 = Card()
        card1.create_card()
        card2 = Card()
        card2.create_card()
        assert card1 == card2

    def test_ne(self):
        card1 = Card()
        card1.create_card()
        card2 = Card()
        card2.create_card()
        assert card1 != card2


class TestBarrel:
    def test_barrel_in_range(self):
        barrel = Barrel()
        for i in range(90): barrel.get_number()
        assert all(ele >= 1 and ele < 91 for ele in barrel.barrels_list) == True

    def test_left_barrels(self):
        barrel = Barrel()
        barrel.get_number()
        assert barrel.left_barrels == 90 - 1

    def test_count_barrels(self):
        barrel = Barrel()
        barrel.get_number()
        assert barrel.count_barrel == 1

    def test_eq(self):
        barrel1 = Barrel()
        barrel1.get_number()
        barrel2 = Barrel()
        barrel2.get_number()
        assert barrel1 == barrel2

    def test_ne(self):
        barrel1 = Barrel()
        barrel1.get_number()
        barrel2 = Barrel()
        barrel2.get_number()
        assert barrel1 == barrel2

    def test_call(self):
        new_barrel = Barrel()
        new_barrel.get_number()
        assert new_barrel.number_barrel == new_barrel()


class TestPlayer:
    def test_name_player(self):
        player = Player('Anton')
        assert player.name == 'Anton'

    def test_player_card(self):
        player = Player('Anton')
        player.new_card()
        assert len(player.play_card.card_create) == 15

    def test_eq(self):
        player1 = Player("Anton")
        player1.new_card()
        player2 = Player("Ivan")
        player2.new_card()
        assert player1 == player2
    def test_ne(self):
        player1 = Player("Anton")
        player1.new_card()
        player2 = Player("Ivan")
        player2.new_card()
        assert player1 != player2
