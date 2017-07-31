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

def test_take_away():
    l = [
        ['1', 'Princess_Castle', 50, 650.0, 1250.0],
        ['2', 'Blast_Zone', 50, 1000.0, 2000.0],
        ['3', 'Jump_Slide', 50, 1400.0, 2500.0]
    ]
    assert core.take_away('Princess_Castle', 650.0, l) == True


# def test_message_log():
#     assert core.message_log('1', 'Princess_Castle', 50, 650.0, 1250.0) == '1, Princess_Castle, 50, 650.0, 1250.0\n'
#     assert core.message_log('2', 'Blast_Zone', 50, 1000.0, 2000.0) == '2, Blast_Zone, 50, 1000.0, 2000.0\n'
#     assert core.message_log('3', 'Jump_Slide', 50, 1400.0, 2500.0) == '3, Jump_Slide, 50, 1400.0, 2500.0\n'
