from os import system, name

from tabulate import tabulate
import lib.saves_proc as sp

class Market:
    @staticmethod
    def welcome():
        x = input("\nWelcome to the market! I'm Benedict. Is this your first time here? y/n ")

        if x != 'y' and x != 'n':
            print("Please enter y or n\n")
            Market.welcome()
        elif x == 'y':
            input("\nSince this is your first time, let me give you a quick rundown on how things work here.\nI "
                  "will shortly provide you with a menu, and from that menu you can buy things that you need in order "
                  "to sustain yourself.\nThrough the credit system recently adapted here, you do not have to have your "
                  "pay ready at the moment you buy the item.\nRemember, you need food for the winter, so don't leave "
                  "this market for the first time without buying something\nBe careful not to get into too much debt!"
                  "\nPress ENTER to view the menus. ")
        elif x == 'n':
            temp = input("Well, you already know what to do. \nPress ENTER to view the menus")

    @staticmethod
    def menu_display():
        print(tabulate(
            [["1", "Wheat (per bushel)", "0.60"], ["2", "Corn (per bushel)", "1.00"], ["3", "Rye (per bushel)", "0.75"],
             ["4", "Beans (per bushel)", "1.50"], ["5", "Pork (per pound)", "0.06¼"], ["6", "Salt shad", "0.14"],
             ["7", "Broadcloth (per yard", "2.50"], ["8", "Firearms", "100"], ["9", "Land (plot)", "1,200.00"]]
            ["No.", "Item", "Price"],
            tablefmt="grid"))

    @staticmethod
    def buy(debt):
        item = int(input("Enter the No. of your desired item to begin the transaction... "))
        while item != 1 and item != 2 and item != 3 and item != 4 and item != 5 and item != 6:
            print("\nPlease enter a number from 1-6")
            item = int(input("Enter the No. of your desired item to begin the transaction... "))

        number = int(input("How many of this item will you be purchasing? "))

        if item == 1:
            cost = number * 0.60
        elif item == 2:
            cost = number
        elif item == 3:
            cost = number * 0.75
        elif item == 4:
            cost = number * 1.5
        elif item == 5:
            cost = number * 0.0625
        elif item == 6:
            cost = number * 0.14
        else:
            "Wow, something went seriously wrong and you managed to break the program. I guess you won!"
            exit()

        debt -= cost
        return debt

    @staticmethod
    def sell(debt):
        item = int(input("Enter the No. of your desired item to begin the transaction... "))
        while item != 1 and item != 2 and item != 3 and item != 4 and item != 5 and item != 6:
            print("\nPlease enter a number from 1-6")
            item = int(input("Enter the No. of your desired item to begin the transaction... "))

        number = int(input("How many of this item will you be selling? "))

        if item == 1:
            profit = number * 0.60
        elif item == 2:
            profit = number
        elif item == 3:
            profit = number * 0.75
        elif item == 4:
            profit = number * 1.5
        elif item == 5:
            profit = number * 0.0625
        elif item == 6:
            profit = number * 0.14
        else:
            "Wow, something went seriously wrong and you managed to break the program. I guess you won!"
            exit()
        debt += profit

        print("TRANSACTION CONNECT")
        return debt

    @staticmethod
    def ask_to_keep_going():
        keep_going = input("Would you like to stay in the market? (y/n) ")
        while keep_going != "y" and keep_going != "n":
            print("\nPlease enter either y or n")
            keep_going = input("\nWould you like to stay in the market? (y/n) ")
        if keep_going == "y":
            return True
        if keep_going == "n":
            return False


def main():
    save_file = "saves/market.sf"

    debt = 0

    Market.welcome()

    Market.menu_display()

    buy_or_sell = input("Will you be buying or selling? (b/s) ")
    while buy_or_sell != "b" and buy_or_sell != "s":
        print("\nPlease enter a value b or s")
        buy_or_sell = input("Will you be buying or selling? (b/s) ")

    if buy_or_sell == "b":
        debt = Market.buy(debt)
    elif buy_or_sell == "s":
        debt = Market.sell(debt)

    # let them stay for as long as they want
    keep_going = Market.ask_to_keep_going()

    while keep_going:
        print("\n")
        Market.menu_display()

        buy_or_sell = input("Will you be buying or selling? (b/s) ")
        while buy_or_sell != "b" and buy_or_sell != "s":
            print("\nPlease enter a value b or s")
            buy_or_sell = input("Will you be buying or selling? (b/s) ")

        if buy_or_sell == "b":
            debt = Market.buy(debt)
        elif buy_or_sell == "s":
            debt = Market.sell(debt)

        Market.ask_to_keep_going()

    sp.write_dict(save_file, {"Debt": debt})