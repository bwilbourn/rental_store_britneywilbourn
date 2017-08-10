import new_core


def test_make_purchase():
    l = [['1', 'Princess_Castle', 50, 650.0, 1250.0],
         ['2', 'Blast_Zone', 50, 1000.0, 2000.0]]
    assert new_core.make_purchase('Princess_Castle', 1, l) == 820.5
    assert new_core.make_purchase('1', 1, l) == 820.5


def test_rental_price():
    assert new_core.rental_price(1) == 'Your rent total: $1.00'


def test_get_deposit_cost():
    l = [['1', 'Princess_Castle', 50, 650.0, 1250.0],
         ['2', 'Blast_Zone', 50, 1000.0, 2000.0]]
    assert new_core.get_deposit_cost(l) == 125.0


def test_deposit_price():
    assert new_core.deposit_price(1) == 'Your deposit total is: $1.00'


def test_make_history():
    l = [['1', 'Princess_Castle', 50, 650.0, 1250.0],
         ['2', 'Blast_Zone', 50, 1000.0, 2000.0]]
    assert new_core.make_history(l, '1') == 650.0


def test_minus_inventory():
    l = [['1', 'Princess_Castle', 50, 650.0, 1250.0],
         ['2', 'Blast_Zone', 50, 1000.0, 2000.0]]
    assert new_core.minus_inventory(
        '1', 1, l
    ) == 'code, house, quantity, rent, replace\n1, Princess_Castle, 49, 650.0, 1250.0\n2, Blast_Zone, 50, 1000.0, 2000.0'


def test_get_return_deposit_cost():
    assert new_core.get_return_deposit_cost(
        1) == 'Total deposit returned back: $1.00'


def test_make_return_history():
    l = [['1', 'Princess_Castle', 50, 650.0, 1250.0],
         ['2', 'Blast_Zone', 50, 1000.0, 2000.0]]
    assert new_core.make_return_history(l, '1', 2, 65) == 65


def test_return_rental():
    l = [['1', 'Princess_Castle', 50, 650.0, 1250.0],
         ['2', 'Blast_Zone', 50, 1000.0, 2000.0]]
    assert new_core.return_rental(
        '1', 1, l
    ) == 'code, house, quantity, rent, replace\n1, Princess_Castle, 51, 650.0, 1250.0\n2, Blast_Zone, 50, 1000.0, 2000.0'
