import csv


def read_values(file_path):
    with open(file_path, newline='') as savefile:
        savefile_reader = csv.DictReader(savefile, delimiter=',')
        value_dict = {}
        for row in savefile_reader:
            value_dict[row['Var']] = row['Value']
        return value_dict


def write_values(file_path, values_to_write):
    with open(file_path, 'w', newline='') as savefile:
        savefile_writer = csv.DictWriter(savefile, fieldnames=["Var", "Value"], delimiter=',')
        savefile_writer.writeheader()
        for rows in values_to_write:
            savefile_writer.writerow(values_to_write)
