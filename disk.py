def open_inventory():
    inventory = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], split_string[1], split_string[2], float(split_string[3]), float(split_string[4])])
    return inventory

def change_inventory(msg):
    with open('inventory.txt', 'w') as file:
        file.write(msg)
    return True


def write_log(log, decision, quantity):
    msg = '{}, {}, {}\n'.format(decision, quantity, log)
    with open('history.txt', 'a') as file:
        file.write(msg)

