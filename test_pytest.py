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


class TestBarrel:
    def test_barrel_in_range(self):
        barrel = Barrel()
        for i in range(90): barrel.get_number()
        assert all(ele >= 1 and ele < 91 for ele in barrel.barrels_list) == True

    def test_left_barrels(self):
        barrel = Barrel()
        barrel.get_number()
        assert barrel.left_barrels == 90 - 1


class TestPlayer:
    def test_name_player(self):
        player = Player('Anton')
        assert player.name == 'Anton'
    def test_
