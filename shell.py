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
    decision = input(message)
    while True:
        if decision == 'return':
            choice = input('''Which rental are you returning?\n
            \t1. Princess_Castle $650.0
            \t2. Blast_Zone $1000.0
            \t3. Jump_Slide $1400.0
            \t4. Sports_Zone $280.0
            \t5. Safari_Bounce $430.0''')
            quantity = int(input('How many would you like to return? ').strip())
            msg = core.return_rental(choice, quantity, inventory)
            disk.change_inventory(msg)
            print('Returned! Have a great day!')
            exit()

    while True:
        if decision.lower().strip() == 'q':
            print('Goodbye!')
            break
        quantity = int(input('How many would you like? ').strip())
        price = core.make_purchase(decision, quantity, inventory)
        print(core.rental_price(price))
        break
        print('Thank you have a nice day!')

    if core.make_purchase(decision, quantity, inventory):
        print('Successful sale!')

        msg = core.take_away(decision, quantity, inventory)
        disk.change_inventory(msg)
        print('Success!')
        # write message for history
        log = core.make_history(decision, quantity, price)
        # write message to history
        disk.write_log(log, decision, quantity)
        print('That is all!')


if __name__ == '__main__':
    main()