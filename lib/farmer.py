# farmer.py

def main():
    # put the code here
    def farm_choice():
        def choose_farm():
            chosen_farm = int(input("What will your farm focus on?\n1) livestock 2) crops"))
            if chosen_farm != 1 or chosen_farm != 2:
                print("\nPlease enter a valid farm value\n")
                choose_farm()
            return chosen_farm
        farm = choose_farm()

