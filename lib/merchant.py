# merchant.py
# Written by Valmik Revankar

from random import randint
import lib.saves_proc as sp
import lib.market as market
import time

class Merchant:
	price_multiplier = [0, 0]
	market_segment, chosen_merch = 1, 0

	def set_segment(self=None):
		if Merchant.chosen_merch == 1:
			Merchant.price_multiplier = [1.50 * Merchant.market_segment, 12.5 * Merchant.market_segment]
		elif Merchant.chosen_merch == 2:
			Merchant.price_multiplier = [50 * Merchant.market_segment, 125 * Merchant.market_segment]
		elif Merchant.chosen_merch == 3:
			Merchant.price_multiplier = [5000 * Merchant.market_segment, 12500 * Merchant.market_segment]
		elif Merchant.chosen_merch < 3:
			print("Apparently you've managed to break this program.")

	def update_market_segment(self=None):
		Merchant.market_segment += 1
		Merchant.set_segment(Merchant.chosen_merch)

	@staticmethod
	def choose_merch():
		Merchant.chosen_merch = int(input("What will you be selling? Choose from the following:\n1) Clothing\n2) Firearms\n3) Land\nChoose your field: "))
		while Merchant.chosen_merch < 1 or Merchant.chosen_merch > 3:
			Merchant.chosen_merch = int(input("That's an invalid answer choice. What will you be selling? Choose from the following:\n1) Clothing\n2) Firearms\n3) \
											Land\nChoose your field: "))
		Merchant.set_segment(Merchant.chosen_merch)


	def generate_random_price(self):
		return randint(Merchant.price_multiplier[0], Merchant.price_multiplier[1])


def debug():
	Merchant.choose_merch()
	for x in range(5):
		input("\n\nHit ENTER to update market segment")
		Merchant.update_market_segment()
		print("New market segment is " + str(Merchant.market_segment) + ". Prices in your field (number " + str(Merchant.chosen_merch) + ") range from " + str(Merchant.price_multiplier[0]) + " to " + str(Merchant.price_multiplier[1]) + " euros.")


def main():
	save_game_values = {
		'ItemsSold': 0,
		'MoneyInPossession': 0,
		'MerchantType': Merchant.chosen_merch
	}
	save_file = "saves/merchant.sf"
	sp.write_dict(save_file, save_game_values)
	Merchant.choose_merch()
	save_game_values['MerchantType'] = Merchant.chosen_merch
	sp.write_dict(save_file, save_game_values)
	input("Now that you're all set up, hit ENTER to go to the market.")
	market.main()
	save_game_values = sp.read_dict(save_file)
	if not save_game_values['ItemsSold'] % 4 == 0 and Merchant.market_segment < 4:
		Merchant.update_market_segment()
		print("Congrats! You've made your way up in the market. You can now sell higher quality goods or more valuable land.")
	elif save_game_values['ItemsSold'] > 3:
		print("You are already at the maximum tier of sales. Good on you!")
	while True:
		exitS = str(input("Would you like to exit? (y/n)"))
		if exitS == "y":
			break
		input("Press ENTER to sleep the night.")
		print("Good night...")
		time.sleep(5)
		print("Good morning!")
		input("Press ENTER to go to the market. ")
		market.main()
