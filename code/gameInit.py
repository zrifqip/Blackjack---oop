import decks
import os

class game_init :
    
    def __init__(self):
        self.hand = []
        
    def initial_game(self) :
        for i in range(2) :
             decks.decks().shuffle()
             card = decks.decks().draw()
             self.hand.append(card)
        return self.hand

    def total_score(self,deck) :
        score = 0
        for card in deck :
            if card == "J" or card == "K" or card == "Q" :
                score += 10
            elif card == "A":
                if(score > 11) :
                    score += 1
                else :
                    score += 10
            else :
                score += card
        return score