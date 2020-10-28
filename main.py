from lib.satellite import *
import lib.merchant as merchant, lib.farmer as farmer

with open("ascii_art/colonist.txt") as colonist:
    print(colonist.read())

input("PRESS ENTER TO BEGIN")
clear()

# now the fun begins
print("Welcome to Connecticut! You will have the opportunity to meet people and live life like the colonists \
of the mid 18th century.\nThe year is 1768, your name is Henry Smith and you are 17 years old.")
print("\n")
JOB = job_choice()  # found in satellite.py
if JOB == 2:
    merchant.main()
elif JOB == 1:
    farmer.main()
else:
    print("Something went WRONG! Exiting program...")
