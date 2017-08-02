import core, disk

def main():
    inventory = disk.open_inventory()
    print("Welcome to Brits Bounce Rentals!")
    message = """
    Hello! Which Bounce House would you like to rent today or would you like to return a rental?\n
    \t*Price shown is for 3 days*\n
    \t**.10 deposit of replacement value is added to total, 
    \twill be returned to customer if rental is as rented.**\n
    \t1. Princess_Castle $650.0
    \t-replacement cost: $1250.0\n
    \t2. Blast_Zone $1000.0
    \t-replacement cost: $2000.0\n
    \t3. Jump_Slide $1400.0
    \t-replacement cost: $2500.0\n
    \t4. Sports_Zone $280.0
    \t-replacement cost: $550.0\n
    \t5. Safari_Bounce $430.0
    \t-replacement cost: $900.0\n
    \t "return" to return rental.
    \t Press q to quit
    """
    decision = input(message)
    if decision == 'return':
        choice = input('''Which rental are you returning?\n
        \t1. Princess_Castle $650.0
        \t2. Blast_Zone $1000.0
        \t3. Jump_Slide $1400.0
        \t4. Sports_Zone $280.0
        \t5. Safari_Bounce $430.0\n''')
        quantity = int(input('How many would you like to return? ').strip())
        price = core.make_purchase(decision, quantity, inventory)
        msg = core.return_rental(choice, quantity, inventory)
        disk.change_inventory(msg)
        print('Returned! Have a great day!')
        # write message for history
        log = core.make_history(decision, quantity, price)
        # write message to history
        disk.write_log(log, decision, quantity)
        exit()

    elif decision.lower().strip() == 'q':
        print('Goodbye!')
        exit()
    quantity = int(input('How many would you like? ').strip())
    price = core.make_purchase(decision, quantity, inventory)
    print(core.rental_price(price))
    print('Thank you have a nice day!')

    if core.make_purchase(decision, quantity, inventory):
        msg = core.take_away(decision, quantity, inventory)
        disk.change_inventory(msg)
        # write message for history
        log = core.make_history(decision, quantity, price)
        # write message to history
        disk.write_log(log, decision, quantity)
        print('Successful sale.')


if __name__ == '__main__':
    main()