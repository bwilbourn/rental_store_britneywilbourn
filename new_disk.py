def open_inventory():
    inventory = []
    with open('new_inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([
            split_string[0], split_string[1], split_string[2],
            float(split_string[3]),
            float(split_string[4])
        ])
    return inventory


def write_history(decision, quantity, price, deposit, total):
    msg = '{}, {}, {}, {}, {}\n'.format(decision, quantity, price, deposit,
                                        total)
    with open('new_history.txt', 'a') as file:
        file.write(msg)


def change_inventory(message):
    with open('new_inventory.txt', 'w') as file:
        file.write(message)
    return True


def write_return_history(return_decision, return_quantity, return_deposit,
                         return_total):
    log = '{}, {}, {}, {}\n'.format(return_decision, return_quantity,
                                    return_deposit, return_total)
    with open('new_history.txt', 'a') as file:
        file.write(log)
