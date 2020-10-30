from lib.satellite import *
import lib.merchant as merchant, lib.farmer as farmer, lib.saves_proc as sp

with open("ascii_art/colonist.txt") as colonist:
    print(colonist.read())

input("PRESS ENTER TO BEGIN")
clear()

JOB_tracking = "saves/player.sf"

# clear previous saves
empty = {}
merchant_tracking = "saves/merchant.sf"
sp.write_dict(merchant_tracking, empty)

farmer_tracking = "saves/farmer.sf"
sp.write_dict(farmer_tracking, empty)

market_tracking = "saves/market.sf"
sp.write_dict(market_tracking, {'Debt': 0})

player_tracking = "saves/player.sf"
sp.write_dict(player_tracking, empty)

# now the fun begins
print("Welcome to Connecticut! You will have the opportunity to meet people and live life like the colonists \
of the mid 18th century.\nThe year is 1768, your name is Henry Smith and you are 17 years old.\n")
JOB = job_choice()  # found in satellite.py
if JOB == 2:
    sp.write_dict(JOB_tracking, {'Job': 2})
    merchant.main()
elif JOB == 1:
    sp.write_dict(JOB_tracking, {'Job': 1})
    farmer.main()
else:
    print("Something went WRONG! Exiting program...")
