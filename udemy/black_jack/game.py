playing = True


def take_bet(chips):
	while True:
		try:
			chips.bet = int(input('How many chips would you like to bet?'))
		except ValueError:
			print('Pls provide an int.')
		else:
			if chips.bet > chips.total:
				print(f'Not enough chips. You have: {chips.total}')
			else:
				break


def hit(deck, hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace()


def hit_or_stand(deck, hand):
	global playing

	while True:
		x = input('Hit or Stand? Enter H or S.')
		if x[0].lower() == 'h':
			hit(deck, hand)
		elif x[0].lower() == 's':
			print("Played stands. Dealer's turn")
			playing = False
		else:
			print('Wrong input.')
			continue
		break


def player_busts(player, dealer, chips):
	print('Bust player.')
	chips.lose_bet()


def player_wins(player, dealer, chips):
	print('Player wins.')
	chips.win_bet()


def dealer_busts(player, dealer, chips):
	print('Player wins. Dealer busted.')
	chips.win_bet()


def dealer_wins(player, dealer, chips):
	print('Dealer wins.')
	chips.lose_bet()


def push(player, dealer):
	print('Dealer and player tie. Push.')


def show_some(player, dealer):
	print("Dealer's hand:\nOne card hidden.")
	print(dealer.cards[1])
	print("\nPlayer's hand:")
	for card in player.cards:
		print(card)


def show_all(player, dealer):
	print("Dealer's hand:\nOne card hidden.")
	for card in dealer.cards:
		print(card)
	print("\nPlayer's hand:")
	for card in player.cards:
		print(card)
