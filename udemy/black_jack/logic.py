from udemy.black_jack.deck import Deck
from udemy.black_jack.hand import Hand
from udemy.black_jack.chips import Chips
from udemy.black_jack.game import *

while True:
	print('Welcome to BlackJack.')
	deck = Deck()  # prepare deck
	deck.shuffle()

	# create player and dealer
	player_hand = Hand()
	for i in range(2):
		player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	for i in range(2):
		dealer_hand.add_card(deck.deal())

	# give chips to player
	player_chips = Chips()

	# let's start
	take_bet(player_chips)
	show_some(player_hand, dealer_hand)

	while playing:
		hit_or_stand(deck, player_hand)
		show_some(player_hand, dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand, dealer_hand, player_chips)
			break

	if player_hand.value <= 21:
		while dealer_hand < player_hand.value:
			hit(deck, dealer_hand)

		show_all(player_hand, dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)
		else:
			push(player_hand, dealer_hand)

	print(f'\nPlayer total chips: {player_chips.total}')

	new_game = input('Would you like to play a new game? Y or N')
	if new_game[0].lower() == 'y':
		playing = True
	else:
		print('Thx')
		break