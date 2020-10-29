# merchant.py
# Written by Valmik Revankar

class Merchant:
	price_multiplier = [0, 0]
	market_segment = 1

	def update_market_segment(self, chosen_merch):
		market_segment = self.market_segment
		market_segment += 1
		if chosen_merch == 1:
			price_multiplier = [1.50 * self.market_segment, 12.5 * self.market_segment]
		elif chosen_merch == 2:
			price_multiplier = [50 * self.market_segment, 125 * self.market_segment]
		elif chosen_merch == 3:
			price_multiplier = [5000 * self.market_segment, 12500 * self.market_segment]
		elif chosen_merch < 3:
			print("Apparently you've managed to break this program.")

	def choose_merch(self=None):
		chosen_merch = int(input("What will you be selling? Choose from the following:\n1) Clothing\n2) Firearms\n3) \
								Land\nChoose your field: "))

		while chosen_merch < 1 or chosen_merch > 3:
			chosen_merch = int(input("That's an invalid answer choice. What will you be selling? Choose from the following:\n1) Clothing\n2) Firearms\n3) \
											Land\nChoose your field: "))

		if chosen_merch == 1:
			price_multiplier = [1.50 * self.market_segment, 12.5 * self.market_segment]
		elif chosen_merch == 2:
			price_multiplier = [50 * self.market_segment, 125 * self.market_segment]
		elif chosen_merch == 3:
			price_multiplier = [5000 * self.market_segment, 12500 * self.market_segment]
		elif chosen_merch < 3:
			print("Apparently you've managed to break this program.")


def main():
	Merchant.choose_merch()
