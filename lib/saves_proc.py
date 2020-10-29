def write_dict(text, dict_in):
    with open(text, "w") as f:
        f.write(str(dict_in))
    f.close()


def read_dict(text):
    with open(text, "r") as f:
        return eval(f.read())
