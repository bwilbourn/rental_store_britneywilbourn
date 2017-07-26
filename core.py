def make_purchase(item, quantity, inventory):
    """ (str, float) -> float
    Print name of bounce house(s) and total amount spent. 

    >>> make_purchase('1', 1)
    695.5
    >>> make_purchase('2', 1)
    1070.0
    >>> make_purchase('3', 1)
    1498.0
    >>> make_purchase('4', 1)
    299.6
    >>> make_purchase('5', 1)
    460.1
    """
    sales_tax = 1.07
    for house in inventory:
        if house[1] == item:
            return float(650.0 * quantity * sales_tax + house[2] * .10)

# def replacement_cost(replace):
#     """int -> int
    
#     >>> replacement_cost('Princess_Castle')
#     1250.0
#     >>> replacement_cost('Blast_Zone')
#     2000.0
#     >>> replacement_cost('Jump_Slide')
#     2500.0
#     >>> replacement_cost('Sports_Zone')
#     550.0
#     >>> replacement_cost('Safari_Bounce')
#     900.0
#     """
#     l = [ 
#         ['1', 'Princess_Castle', 1250.0]
#         ['2', 'Blast_Zone', 2000.0]
#         ['3', 'Jump_Slide', 2500.0]
#         ['4', 'Sports_Zone', 550.0]
#         ['5', 'Safari_Bounce', 900.0]
#     ]
#     for item in l:
#         if item == '1' or item == 'Princess_Castle':
#             return 1250.0
#         elif item == '2' or item == 'Blast_Zone':
#             return 2000.0
#         elif item == '3' or item == 'Jump_Slide':
#             return 2500.0
#         elif item == '4' or item == 'Sports_Zone':
#             return 550.0
#         elif item == '5' or item == 'Safari_Bounce':
#             return 900.0 
    
        

def rental_price(price):
    """(int) -> string"""
    if price == str(price):
        return 'Invalid choice.'
    return 'Your rent total: ${:.2f}'.format(float(price))

# def return_rental():