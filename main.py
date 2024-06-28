from deck import Deck
from hand import Hand
from chips import Chips

playing = True


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have: {chips.total}")
            else:
                break


def hit(dec, hand):

    single_card = dec.deal_one()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(dec, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(dec, hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, Please enter h or s only!")
            continue

        break


def show_some(player, dealer):
    # dealer.playing_cards[o]
    # Show only ONE of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.playing_cards[1])

    # Show all (2 cards) of the player's hand/cards
    print("\n Player's hand:")
    for card in player.playing_cards:
        print(card)


def show_all(player, dealer):

    # Show all Dealer's cards
    print("\n Dealer's hand:")
    for card in dealer.playing_cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")

    # Show all player's cards
    print("\n Player's hand:")
    for card in player.playing_cards:
        print(card)
    # calculate and display value (j+k == 20)
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print(f"DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie! PUSH')


# Set up the Player's chips
player_chips = Chips()

while True:
    # Game setup

    print("WELCOME TO BLACKJACK")
    # create & shuffle the deck, deal two cards to player and two to dealer
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show some cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # prompt player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform player of their chips total
    print(f'\n Player total chips are at: {player_chips.total}')
    # Ask to play again
    new_game = input("Would you like to play another hand? y/n:  ")

    if new_game[0].lower() == 'y':
        playing = True

        continue
    else:
        print('Thank you for playing!')
        break
