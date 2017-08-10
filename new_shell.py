import new_core, new_disk


def main():
    inventory = new_disk.open_inventory()
    print("Welcome to Brits Bounce Rentals!")
    yes_no = input("Would you like to rent a Bounce House? ")
    if yes_no == 'yes':
        decision = input(
            '''Please enter which bounce house you would like to rent.\n
        \t1. Princess_Castle $650.0
        \t2. Blast_Zone $1000.0
        \t3. Jump_Slide $1400.0
        \t4. Sports_Zone $280.0
        \t5. Safari_Bounce $430.0\n''')
        quantity = int(input('How many would you like? ').strip())
        price = new_core.make_purchase(decision, quantity, inventory)
        print('We have a 10% deposit that will be returned later.')
        deposit = new_core.get_deposit_cost(inventory)
        # writes message for history
        total = new_core.make_history(inventory, decision)
        # writes message to history
        new_disk.write_history(decision, quantity, price, deposit, total)

        # function for inventory to change
        message = new_core.minus_inventory(decision, quantity, inventory)

        # makes inventory quantity change
        new_disk.change_inventory(message)

        print(new_core.deposit_price(deposit))
        print(new_core.rental_price(price))
        print('Thank you! Have lots of bouncy fun! ')
        exit()
    elif yes_no == 'no':
        return_decision = input(
            '''Please enter which bounce house you would like to return.\n
        \t1. Princess_Castle
        \t2. Blast_Zone
        \t3. Jump_Slide
        \t4. Sports_Zone
        \t5. Safari_Bounce\n''')
        return_quantity = int(
            input('How many would you like to return? ').strip())
        return_deposit = new_core.get_deposit_cost(inventory)
        # print(new_core.get_return_deposit_cost(return_deposit))

        # writes message for history
        return_total = new_core.make_return_history(
            inventory, return_decision, return_quantity, return_deposit)

        # writes message to history
        new_disk.write_return_history(return_decision, return_quantity,
                                      return_deposit, return_total)

        # function for inventory to change
        message = new_core.return_rental(return_decision, return_quantity,
                                         inventory)

        # makes inventory quantity change
        new_disk.change_inventory(message)
        print(new_core.get_return_deposit_cost(return_deposit))
        print('Thank you for your business!')
        exit()

    elif yes_no == 'rev':
        print(new_disk.revenue())
        print('is your total revenue.')
        exit()

    elif yes_no == 'q' or yes_no == 'Q':
        print('Goodbye!')
        exit()


if __name__ == '__main__':
    main()