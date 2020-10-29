from lib.csv_proc import *

test_dict = {
    'Var': [0, 1, 2, 3, 4],
    'Value': [1, 2, 3, 4, 5]
}

write_values("saves/market.csv", test_dict)
