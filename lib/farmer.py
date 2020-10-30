# farmer.py
# Written by Muhammad Ibrahim

import lib.market as market
import lib.saves_proc as sp
import time

class Farmer:
    # choose the type of farm
    @staticmethod
    def choose_farm():
        farm = int(input("What will your farm mostly be for?\n1) livestock \n2) crops\nEnter your choice (1 or "
                         "2) "))
        if farm != 1 and farm != 2:
            print("\nPlease enter a valid farm value\n")
            Farmer.choose_farm()

        # deal with choices and force user to go to the market
        if farm == 1:
            input(
                "\nYour farm has 4 horses, 25 cattle, 15 sheep, and 13 pigs. Today you need to go into the market and "
                "buy some items.\nPress ENTER to go to the Market")
        elif farm == 2:
            input("\nYou have a few cattle, sheep, and pigs, but most of your farm is for beans, corn, squash, and wheat. "
                  "Today you need to go into the market and buy some items\nPress ENTER to go to the Market")


def main():
    save_game_values = {'Debt': 0}
    save_file = "saves/market.sf"
    sp.write_dict(save_file, save_game_values)

    Farmer.choose_farm()
    market.main()

    print(".........................................................................................")
    time.sleep(5)
    print("Some time has passed. The winter is almost upon us, and there is still time to stock up on item you might"
          " need.\nHopefully, you have been keeping track of your debt, and you have sold enough of your crop yield to "
          "stay in the black. \nYou now have two choices. You can choose to finish the game, or go to sleep and visit"
          " the market in the morning on last time to try and get out of any possible debt.")
    temp = input("Go back to the market? (y/n) ")
    while temp != "y" and temp != "n":
        print("\nPlease enter either y or n")
        temp = input("Go back to the market? (y/n) ")

    if temp == "y":
        print("Goodnight")
        time.sleep(5)
        print("Good morning! Taking you to the market...")
        time.sleep(3)
        market.main()
    if temp == "n":
        print("If you're sure...")
        time.sleep(3)

    print()