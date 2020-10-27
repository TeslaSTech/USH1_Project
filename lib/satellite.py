from os import system, name

chosen_merch = None
chosen_buy = None


def clear():  # Clear screen function
    # for windows users
    if name == 'nt':
        _ = system('cls')
        # for mac and linux users (here, os.name is 'posix')
    else:
        _ = system('clear')


def job_choice():  # choices
    job = ""

    def choose_job():
        chosen_job = int(input("Choose a job:\n1) Farmer\n2) Merchant\nEnter your choice (1 or 2): "))
        if chosen_job != 1 and chosen_job != 2:
            print("\nPlease input a valid job value\n")
            chosen_job = choose_job()
        return chosen_job
    selected_job = choose_job()
    if selected_job == 1:
        job = "Farmer"
    if selected_job == 2:
        job = "Merchant"
    return job
