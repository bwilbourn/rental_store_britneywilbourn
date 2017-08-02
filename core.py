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
    """(int) -> string"""
    return 'Your rent total: ${:.2f}'.format(float(price))


def take_away(decision, quantity, inventory):
    str_l = ['code, house, quantity, rent, replace']
    for item in inventory:
        if item[0] == decision:
            item[2] = int(item[2]) - quantity
        str_l.append('{}, {}, {}, {}, {}'.format(int(item[0]), item[1], int(item[2]), float(item[3]), float(item[4])))
        msg = '\n'.join(str_l)
    return msg

def return_rental(choice, quantity, inventory):
    """ (int) -> float
    return total rented item to inventory. 
    """
    str_l = ['code, house, quantity, rent, replace']
    for item in inventory:
        if item[0] == choice:
            item[2] = int(item[2]) + quantity
        str_l.append('{}, {}, {}, {}, {}'.format(int(item[0]), item[1], int(item[2]), float(item[3]), float(item[4])))
        inven = '\n'.join(str_l)
    return inven
   

def make_history(decision, quantity, price):
    if decision == '1' or decision == 'Princess_Castle':
        return price
    elif decision == '2' or decision == 'Blast_Zone':
        return price
    elif decision == '3' or decision == 'Jump_Slide':
        return price
    elif decision == '4' or decision == 'Sports_Zone':
        return price
    elif decision == '5' or decision == 'Safari_Bounce':
        return price



        
