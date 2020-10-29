from tabulate import tabulate


class Market:
    @staticmethod
    def welcome():
        x = input("\nWelcome to the market! I'm Benedict. Is this your first time here? y/n ")

        if x != 'y' and x != 'n':
            print("Please enter y or n\n")
            Market.welcome()
        elif x == 'y':
            input("\nSince this is your first time here, let me give you a quick rundown on how things work here.\nI "
                  "will shorty provide you with a menu, and from that menu you can buy things that you need in order "
                  "to sustain yourself.\nThrough the credit system recently adapted here, you do not have to have your "
                  "pay ready at the moment you buy the item.\nBe careful not to get into too much debt! \nPress ENTER "
                  "to view the menus. ")
        elif x == 'n':
            temp = input("Well, you already know what to do. \nPress ENTER to view the menus")

    @staticmethod
    def menu_display():
        print(tabulate(
            [["1", "Wheat per bushel", "0.60"], ["2", "Corn per bushel", "1.00"], ["3", "Rye per bushel", "0.75"],
             ["4", "Beans per bushel", "1.50"], ["5", "Pork per pound", "0.06¼"], ["6", "Salt shad", "0.14"]],
            ["No.", "Item", "Price"],
            tablefmt="grid"))

    @staticmethod
    def buy():
        item = input(int("Enter the No. of your desired item to begin the transaction... "))
        while item != 1 and item != 2 and item != 3 and item != 4 and item != 5 and item != 6:
            print("\nPlease enter a number from 1-6")
            item = input(int("Enter the No. of your desired item to begin the transaction... "))

        number = input(int("How many of this item will you be purchasing?"))

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

    @staticmethod
    def sell():
        item = input("Enter the No. of your desired item to begin the transaction... ")


def main():
    Market.welcome()

    Market.menu_display()

    buy_or_sell = input("Will you be buying or selling? (b/s) ")
    while buy_or_sell != "b" and buy_or_sell != "s":
        print("\nPlease enter a value b or s")
        buy_or_sell = input("Will you be buying or selling? (b/s) ")

    if buy_or_sell == "b":
        Market.buy()
    elif buy_or_sell == "s":
        Market.sell()
