from gameInit import game_init
from result import game_result

def play() :
        player_card = game_init().initial_game()
        dealer_card = game_init().initial_game()
        print("Dealer drew a " + str(dealer_card[0]) + " and a hidden card")
        print("You drew a " + str(player_card[0]) + " and a " + str(player_card[1]))
        game_result().blackjack_result(dealer_card,player_card)
        game_result().player_hit_or_stand(player_card)
        game_result().dealers_hit(dealer_card)
        game_result().compare_card(dealer_card,player_card)

print("WELCOME TO BLACKJACK ")
play()