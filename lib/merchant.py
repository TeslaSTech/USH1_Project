# merchant.py
# Written by Valmik Revankar

import csv

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



def debug():
	Merchant.choose_merch()
	for x in range(5):
		input("\n\nHit ENTER to update market segment")
		Merchant.update_market_segment()
		print("New market segment is " + str(Merchant.market_segment) + ". Prices in your field (number " + str(Merchant.chosen_merch) + ") range from " + str(Merchant.price_multiplier[0]) + " to " + str(Merchant.price_multiplier[1]) + " euros.")
