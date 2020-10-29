from tabulate import tabulate

class Market:
    @staticmethod
    def welcome():
        x = input("Welcome to the market! I'm Benedict. Is this your first time here? y/n ")

        if x != 'y' and x != 'n':
            print("Please enter y or n\n")
            Market.welcome()
        elif x == 'y':
            print("Since this is your first time here, let me give you a quick rundown on how things work here. I "
                  "will shorty provide you with a menu, and from that menu you can buy things that you need in order "
                  "to sustain yourself. Through the credit system recently adapted here, you do not have to have your "
                  "pay ready at the moment you buy the item. Be careful not to get into too much debt! Press ENTER to "
                  "view the menus. ")
        elif x == 'n':
            temp = input("Well, you already know what to do. Press ENTER to view the menus")

    @staticmethod
    def menu_display():
        print(tabulate([["value1", "value2"], ["value3", "value4"], ["value5", "value6"]], ["Item", "Price", "Tax"],
                       tablefmt="grid"))

def main():
    Market.welcome()
    Market.menu_display()
