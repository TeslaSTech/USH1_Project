# merchant.py
# Written by Valmik Revankar

import random
price_multiplier = [0, 0]


def choose_merch():
	chosen_merch = int(input("What will you be selling? Choose from the following:\n1) Clothing\n2) Firearms\n3) "
							 "Land\nChoose your field: "))
	market_segment = random.randint(1,3)
	if chosen_merch == 1:
		price_multiplier = [1.50 * market_segment, 2, 12.5 * market_segment, 2]


def main():
	choose_merch()