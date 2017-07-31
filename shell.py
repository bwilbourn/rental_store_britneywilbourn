import core, disk

def main():
    inventory = disk.open_inventory()
    # print(inventory)
    print("Welcome to Brits Bounce Rentals 4 You!")
    message = """
    Hello! Which Bounce House would you like to rent today or will you be returning a rental?
    \t **Price shown is for 3 days**
    \t *** .10 deposit of replacement value is added to total, 
    \t     is returned to customer if rental is as rented. ***
    \t1. Princess_Castle $650.0
    \t2. Blast_Zone $1000.0
    \t3. Jump_Slide $1400.0
    \t4. Sports_Zone $280.0
    \t5. Safari_Bounce $430.0
    \t "return" to return rental.
    \t Press q to quit
    """
    while True:
        decision = input(message)
        if decision.lower().strip() == 'q':
            print('Goodbye!')
            break
        quantity = int(input('How many would you like? ').strip())
        price = core.make_purchase(decision, quantity, inventory)
        print(core.rental_price(str(price)))
        break
    print('Thank you have a nice day!')

    if core.make_purchase(decision, quantity, inventory):
        print('Successful sale!')
    if core.take_away(decision, quantity, inventory):
        print('Success!')


if __name__ == '__main__':
    main()