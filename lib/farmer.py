# farmer.py

def main():
    farm = None

    # choose the type of farm
    def choose_farm():
        chosen_farm = int(input("What will your farm mostly be for?\n1) livestock \n2) crops"))
        if chosen_farm != 1 or chosen_farm != 2:
            print("\nPlease enter a valid farm value\n")
            choose_farm()
        return chosen_farm

    farm = choose_farm()

    if farm == 1:
        input("\nYour farm has 4 horses, 25 cattle, 15 sheep, and 13 pigs. Today you need to go into the market and "
              "buy some items. "
              "\nPress ENTER to go to the market")
