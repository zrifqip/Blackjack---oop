from gameInit import game_init
from decks import decks

class game_result :
    def __init__(self) :
        pass
    def blackjack_result(self,dealerdeck,playerdeck) :
        if game_init().total_score(dealerdeck) == 21 :
            if game_init().total_score(playerdeck) == 21 :
                print('PUSH')
                exit()
            else :
                print('DEALERS BLACKJACK')
                exit()
        elif game_init().total_score(playerdeck) == 21:
            print('BLACKJACK')
            exit()

    def player_hit_or_stand(self,player_card) :
        select = input("Hit Or Stand : ").lower()
        while select == "hit" and game_init().total_score(player_card) < 22 :
            card = decks().draw()
            player_card.append(card)
            print("you drew a " + str(card))
            if game_init().total_score(player_card) > 21 :
                print ("Your Total : {} ".format(game_init().total_score(player_card)))
                print("Your Card : {}".format(player_card))
                print('BUSTED')
                exit()
            else :
                print ("Your Total : {} ".format(game_init().total_score(player_card)))
                print("Your Card : {}".format(player_card))
                select = input("Hit Or Stand : ").lower()
        if select == "stand" :
            print("You Stood")
        else :
            print("invalid answer")
            exit()
        return player_card

    def dealers_hit(self,dealer_card) :
        while game_init().total_score(dealer_card) < 17 :
            card = decks().draw()
            dealer_card.append(card)
            print("dealer drew a {}".format(card))
            if game_init().total_score(dealer_card) > 21:
                print ("Dealer Total : {} ".format(game_init().total_score(dealer_card)))
                print("Dealer Card : {}".format(dealer_card))
                print("DEALER BUSTED, YOU WON!")
                exit()
        return dealer_card

    def compare_card(self,dealer_card,player_card):
        if(game_init().total_score(dealer_card) == game_init().total_score(player_card)) :
            print ("Your Total : {} ".format(game_init().total_score(player_card)))
            print("Your Card : {}".format(player_card))
            print ("Dealer Total : {} ".format(game_init().total_score(dealer_card)))
            print("Dealer Card : {}".format(dealer_card))
            print('PUSH')
        elif(game_init().total_score(dealer_card) < game_init().total_score(player_card)) :
            print ("Your Total : {} ".format(game_init().total_score(player_card)))
            print("Your Card : {}".format(player_card))
            print ("Dealer Total : {} ".format(game_init().total_score(dealer_card)))
            print("Dealer Card : {}".format(dealer_card))
            print('YOU WON!')
        elif(game_init().total_score(dealer_card) > game_init().total_score(player_card)) :
            print ("Your Total : {} ".format(game_init().total_score(player_card)))
            print("Your Card : {}".format(player_card))
            print ("Dealer Total : {} ".format(game_init().total_score(dealer_card)))
            print("Dealer Card : {}".format(dealer_card))
            print('YOU LOST!')
        exit()
