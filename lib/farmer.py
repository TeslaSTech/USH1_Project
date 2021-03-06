# farmer.py
# Written by Muhammad Ibrahim

import lib.market as market
import lib.saves_proc as sp
import time


class Farmer:
    market_file = "saves/market.sf"
    market_savefile = sp.read_dict(market_file)
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
            return 1
        elif farm == 2:
            input(
                "\nYou have a few cattle, sheep, and pigs, but most of your farm is for beans, corn, squash, and wheat."
                "\nToday you need to go into the market and buy some items\nPress ENTER to go to the Market")
            return 2

def main():
    save_file = "saves/farmer.sf"
    farm_type = Farmer.choose_farm()
    save_game_values = {'FarmerType': farm_type}
    sp.write_dict(save_file, save_game_values)
    time.sleep(2)
    market.main()

    print(".........................................................................................")
    time.sleep(5)
    print("Some time has passed. The winter is almost upon us, and there is still time to stock up on item you might"
          " need.\nHopefully, you have been keeping track of your debt, and you have sold enough of your crop yield to "
          "stay in the black. \nYou now have two choices. You can choose to finish the game, or go to sleep and visit"
          " the market in the morning one last time to try and get out of any possible debt.")
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
        if Farmer.market_savefile['Debt'] < 0:
            print(
                "You're in debt! You need to pay this off immediately by selling some items. Back to the market with you!")
            time.sleep(2)
            market.main()
        else:
            print("Congrats, you are not in debt. Thanks for playing!")
            time.sleep(3)

    print()
