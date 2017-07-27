import core

def test_make_purchase():
    l = [
        ['1', 'Princess_Castle', 50, 650.0, 1250.0],
        ['2', 'Blast_Zone', 50, 1000.0, 2000.0]
    ]
    assert core.make_purchase('Princess_Castle', 1, l) == 820.5
    assert core.make_purchase('1', 1, l) == 820.5
    assert core.make_purchase('BZ', 1, l) == 'Invalid'

def test_rental_price():
    assert core.rental_price(1) == 'Your rent total: $1.00'