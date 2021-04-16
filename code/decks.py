import random

deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4
class decks :
    def __init__(self) :
        pass
    def shuffle(self) :
        random.shuffle(deck)
    def draw(self) :
        draw_cards = deck.pop()
        return draw_cards


    

    