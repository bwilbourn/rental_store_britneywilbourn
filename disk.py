def open_inventory():
    inventory = []
    with open('inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        inventory.append([split_string[0], split_string[1], split_string[2], float(split_string[3]), float(split_string[4])])
    return inventory



    # houses = [ 
    #     ['1', 'Princess_Castle', 1250.0],
    #     ['2', 'Blast_Zone', 2000.0],
    #     ['3', 'Jump_Slide', 2500.0],
    #     ['4', 'Sports_Zone', 550.0],
    #     ['5', 'Safari_Bounce', 900.0]
    # ]
