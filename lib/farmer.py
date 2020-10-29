# farmer.py
# Written by Muhammad Ibrahim

import lib.market as market


# choose the type of farm
def choose_farm():
    chosen_farm = int(input("What will your farm mostly be for?\n1) livestock \n2) crops\nEnter your choice (1 or "
                            "2) "))
    if chosen_farm != 1 and chosen_farm != 2:
        print("\nPlease enter a valid farm value\n")
        choose_farm()
    return chosen_farm
    farm = choose_farm()

    # deal with choices and force user to go to the market
    if farm == 1:
        input("\nYour farm has 4 horses, 25 cattle, 15 sheep, and 13 pigs. Today you need to go into the market and "
              "buy some items.\nPress ENTER to go to the Market")
        market.main()
    elif farm == 2:
        input("\nYou have a few cattle and sheep, but most of your farm is for beans, corn, pumpkins, squash, "
              "and rye. Today you need to go into the market and buy some items\nPress ENTER to go to the Market")
        market.main()


def main():
    choose_farm()
