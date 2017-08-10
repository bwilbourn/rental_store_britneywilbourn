def make_purchase(decision, quantity, inventory):
    """ (str, float) -> float
    return total amount spent. 
    """
    sales_tax = 1.07
    for house in inventory:
        if house[0] == decision or house[1] == decision:
            return house[3] * quantity * sales_tax + house[4] * .10
    return 'Invalid'


def rental_price(price):
    """(int) -> float"""
    return 'Your rent total: ${:.2f}'.format(float(price))


def get_deposit_cost(inventory):
    """int -> float"""
    for house in inventory:
        return house[4] * .10


def deposit_price(deposit):
    """(int) -> float"""
    return 'Your deposit total is: ${:.2f}'.format(float(deposit))


def make_history(inventory, decision):
    for house in inventory:
        if decision == house[0] or decision == house[1]:
            return house[3]


def minus_inventory(decision, quantity, inventory):
    str_l = ['code, house, quantity, rent, replace']
    for house in inventory:
        if house[0] == decision:
            house[2] = int(house[2]) - quantity
        str_l.append('{}, {}, {}, {}, {}'.format(
            int(house[0]), house[1],
            int(house[2]), float(house[3]), float(house[4])))
        message = '\n'.join(str_l)
    return message


def get_return_deposit_cost(return_deposit):
    """int -> float"""
    return 'Total deposit returned back: ${:.2f}'.format(float(return_deposit))


def make_return_history(inventory, return_decision, return_quantity,
                        return_deposit):
    for house in inventory:
        if return_decision == house[0] or return_decision == house[1]:
            return return_deposit


def return_rental(return_decision, return_quantity, inventory):
    """ (int) -> float
    return total rented item to inventory.
    """
    str_l = ['code, house, quantity, rent, replace']
    for house in inventory:
        if house[0] == return_decision:
            house[2] = int(house[2]) + return_quantity
        str_l.append('{}, {}, {}, {}, {}'.format(
            int(house[0]), house[1],
            int(house[2]), float(house[3]), float(house[4])))
        inven = '\n'.join(str_l)
    return inven
