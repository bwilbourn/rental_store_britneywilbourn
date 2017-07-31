def open_inventory():
    inventory = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], split_string[1], split_string[2], float(split_string[3]), float(split_string[4])])
    return inventory


# def close_inventory():
#     with open('history.txr', 'w') as file:
#         new_line = ('{}, {}, {}, {}, {}'.format(int(item[0]), item[1], int(item[2]), float(item[3]), float(item[4])))
#         for item in new_line:
#             str_l = new_line.strip()
#             file.write(str_l)