# merchant.py
# Written by Valmik Revankar

from random import randint
import lib.saves_proc as sp
import lib.market as market
import time

class Merchant:

	market_file = "saves/market.sf"
	market_savefile = sp.read_dict(market_file)

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
	back_from_market()


def back_from_market():
	times_ran = 0
	save_file = "saves/merchant.sf"
	Exit = False
	while not Exit:
		Merchant.market_savefile = sp.read_dict(Merchant.market_file)
		print("You came back from the market with a balance of " + str(Merchant.market_savefile['Debt']) + " pounds.")
		if Merchant.market_savefile['Debt'] < 0:
			return_to_market = str(input("You're in debt! Do you want to go back and sell, or is this fine? Keep in mind that if it's been a while, you might have to go back anyway.(y/n)"))
			if times_ran % 3 == 0 or return_to_market == "y":
				if times_ran % 3 == 1:
					print("The time has come to pay your debt. Please go to the market.")
				time.sleep(2)
				market.main()
				times_ran += 1
		save_game_values = sp.read_dict(save_file)
		if not save_game_values['ItemsSold'] % 4 == 0 and Merchant.market_segment < 4:
			Merchant.update_market_segment()
			print("Congrats! You've made your way up in the market. You can now sell higher quality goods or more valuable land.")
		elif save_game_values['ItemsSold'] > 3:
			print("You are already at the maximum tier of sales. Good on you!")
		exitS = str(input("Would you like to exit? (y/n)"))
		if exitS == "y":
			Exit = True
			break
		input("Press ENTER to sleep the night.")
		print("Good night...")
		time.sleep(5)
		print("Good morning!")
		input("Press ENTER to go to the market. ")
		market.main()
		times_ran += 1
