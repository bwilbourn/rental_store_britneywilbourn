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


def return_rental():
    """ float -> (str, float)
    return item into inventory.
    """
    for house in inventory:


# In shell I put "or will you be returning a rental?" at 
# the end of my intro message and
# "\t "return" to return rental." in the "\t" message.



        
