import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
    
class Deck:
    def __init__(self):

        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = [
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "Jack", "value": 10},
            {"rank": "Queen", "value": 10},
            {"rank": "King", "value": 10},
            {"rank": "Ace", "value": 11}
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_to_deal = []
        for _ in range(number):
            if(len(self.cards) > 0):
                cards_to_deal.append(self.cards.pop())
        return cards_to_deal


class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        aces = 0

        for card in self.cards:
            self.value += card.rank['value']
            if card.rank['rank'] == 'Ace':
                aces += 1

        while self.value > 21 and aces:
            self.value -= 10
            aces -= 1

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.value == 21 and len(self.cards) == 2

    def display(self, show_all=False):
        if self.dealer and not show_all:
            print("Dealer's Hand:")
            print(" <card hidden>")
            print('', self.cards[1])
        else:
            print("Dealer's Hand:" if self.dealer else "Player's Hand:")
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())


deck = Deck()
deck.shuffle()

hand = Hand(dealer = True)
hand.add_card(deck.deal(2))
hand.display()