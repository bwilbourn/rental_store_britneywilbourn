import core

def main():
    print("Welcome to Brits Bounce Rentals 4 You!")
    message = """
    Hello! Which Bounce House would you like to rent today?
    \t **Price shown is for 3 days**
    \t1. Princess_Castle $650.0
    \t2. Blast_Zone $1000.0
    \t3. Jump_Slide $1400.0
    \t4. Sports_Zone $280.0
    \t5. Safari_Bounce $430.0
    \t Press q to quit
    """
    while True:
        decision = input(message)
        if decision.lower().strip() == 'q':
            print('Goodbye!')
            break
        quantity = int(input('How many would you like? ').strip())
        price = core.make_purchase(decision, quantity)
        print(core.rental_price(price))
        break
    print('Thank you have a nice day!')


if __name__ == '__main__':
    main()