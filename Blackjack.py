import random

def get_ace(contains_ace):
    if (contains_ace==True):
    ##Ask the player if they want to use a 1 or 11 as their Ace
        value = int(input("You get an Ace Should the Ace be 1 or 11?\n"))

    return value


# card_name = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
# VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10,'K': 10}
# def get_value(player, player_cards):
#     # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
#     value = 0
#
#     for i in range(len(player_cards)):
#         contains_ace = False
#         ## if A will eq=1
#         value += VALUES[player_cards[i]]
#         if (player_cards[i] == 'A'):
#             contains_ace = True
#         if contains_ace and player!="dealer":
#             ace_ctrl+=1 # first time have ace
#             value += get_ace_value(contains_ace)-1# minus the value 1 alreay incremented in previous loop
#         elif contains_ace and player=="dealer" and value+10<21: # borderline case when dealer total=20, he will use ace as 1
#             value+=10
#
#     return value
def get_card(name):

    # get a random number in range 1 to 13
    num = random.randrange(1, 13+1)

    if num == 11 and name=="player":
        contains_ace = True
        return get_ace(contains_ace)
    elif num >10 and num!=11:
        return 10
    else:
        return num



def main():
    print("Game Start \n")
    flag=True
    rounds=0
    while flag==True:

         # Dealer cards
        dealer_cards = []
         # Player cards
        player_cards = []
        #dealer card
        card_num=1
        while len(dealer_cards) != 2:
            dealer_cards.append(get_card("dealer"))
            if len(dealer_cards) == 2:
               print("Dealer has one card and &", dealer_cards[card_num-1])


        # Player Cards
        while len(player_cards) != 2:
            player_cards.append(get_card("player"))
            if len(player_cards) == 2:
                print("You have ", player_cards)

        #get value for dealer and player
        dealer_value=sum(dealer_cards)
        player_value=sum(player_cards)

        #dealer behavior
        while dealer_value<17: #soft hit of 17 for dealer
            dealer_cards.append(get_card("dealer"))
            dealer_value = sum(dealer_cards)

        if dealer_value == 21:
            print("Dealer has 21 and wins!")
            print("The dealer  with " + dealer_cards)

            break
        elif dealer_value > 21:
            print("Dealer has busted!")
            print("The dealer has a total of " + str(dealer_value) + " with ", dealer_cards)
            break

        hitnumber=1
        # player behavior
        while player_value < 21:
            action_taken = str(input("Do you want to stay or hit?  "))
            if action_taken == "hit":
                hitnumber+=1
                player_cards.append(get_card("player"))
                player_value = sum(player_cards)
                print("You now have a total of " + str(player_value) + " from these cards ", player_cards)
                if hitnumber==6:
                    print("reach the maximum hit, finish")
                    # random.shuffle(card_name)
                    # card_num=0
            else:
                print("You have a total of " + str(player_value) + " with ", player_cards)
                if dealer_value > player_value:
                    print("The dealer has a total of " + str(dealer_value) + " with ", dealer_cards)
                    print("Dealer wins!")
                    break

                elif dealer_value==player_value:
                    print("The dealer has a total of " + str(dealer_value) + " with ", dealer_cards)
                    print("Dealer and you tied!" )
                    break

                else:
                    print("You win!")
                    print("The dealer has a total of " + str(dealer_value) + " with ", dealer_cards)
                    break

        if player_value > 21:
            print("You blow! Dealer wins.")
            print("The dealer has a total of " + str(dealer_value) + " with ", dealer_cards)
            break
        elif player_value == 21:
            print("You have BLACKJACK! You Win with ", player_cards)
            break


        return 0





main()
