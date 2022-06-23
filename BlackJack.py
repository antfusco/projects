import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                my_card = Card(suit, rank)
                self.deck.append(my_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck consists of:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        # check ace
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        return self.total

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Place your bet '))
        except:
            print('Invalid Input')
            continue
        else:
            if chips.bet > chips.total:
                print('Not enough funds')
                continue
            else:
                print(f'Bet of {chips.bet} accepted')
                break

def hit(deck,hand):
    single_card = deck.deal()
    print(f"Hit!\nIt's a {single_card}")
    hand.add_card(single_card)
    hand.adjust_for_ace()
    print(f"The total value is {hand.value}")

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        action = input('Hit or Stand? ')
        if action == 'hit' or action == 'Hit':
            hit(deck,hand)
        elif action == 'stand' or action == 'Stand':
            print(f'You have opted to stand, you have a value of {player_hand.value}')
            playing = False
        else:
            print('Invalid input')
            continue
        break

def show_some(player, dealer):
    print(f'The dealer shows {dealer.cards[1]}\nThe player shows {player.cards[0]} and {player.cards[1]}')

def show_all(player, dealer):
    print('The dealer shows:',*dealer.cards,sep='\n')
    print(f"The dealer's total value is {dealer.value}")

    print('The player shows:',*player.cards,sep='\n')
    print(f"The dealer's total value is {player.value}")

def player_busts(chips):
    print('Player busted!')
    chips.lose_bet()

def player_wins(chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(chips):
    print('Dealer busted! Player wins!')
    chips.win_bet()

def dealer_wins(chips):
    print('Dealer wins! Player loses!')
    chips.lose_bet()

def push():
    print('Dealer and Player tie, PUSH!')

player_chips = Chips()
game_on = True
while game_on:
    # Print an opening statement
    print('Time to play blackjack!')

    # Create & shuffle the deck, deal two cards to each player
    my_deck = Deck()
    my_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()
    for num in range(2):
        player_hand.add_card(my_deck.deal())
        dealer_hand.add_card(my_deck.deal())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    playing = True
    while playing:  # recall this variable from our hit_or_stand function
        hit_or_stand(my_deck,player_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        print(f'The dealer flips over their card and reveals a {dealer_hand.cards[0]}')
        while dealer_hand.value < 17:
            hit(my_deck,dealer_hand)

        # Show all cards
        #show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform Player of their chips total
    print(f"The player has {player_chips.total}")

    # Ask to play again
    new_game = 'WRONG'
    while new_game != 'yes' and new_game != 'Yes' and new_game != 'no' and new_game != 'No':
        new_game = input('Play again? ')
        if new_game != 'yes' and new_game != 'Yes' and new_game != 'no' and new_game != 'No':
            print('invalid input')
        elif new_game == 'yes' or new_game == 'Yes':
            continue
        else:
            print('Thanks for playing')
            game_on = False
            break
