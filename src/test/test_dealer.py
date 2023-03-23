from src.jackpot import Gambler, Bid, Dealer


def test_dealer_init_name():
    """
    Should be able to initialize a dealer with
    a name
    """
    dealer = Dealer('Steve')
    assert dealer.name == 'Steve'

def test_dealer_get_name():
    """
    get_name() should return the name of
    the dealer
    """
    dealer = Dealer('Steve')
    assert dealer.get_name() == 'Steve'

def test_dealer_get_bids():
    """
    get_bids() should return the list of bids
    associated with the dealer
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    dealer.bids = [bid]
    assert dealer.get_bids() == [bid]

def test_dealer_get_gamblers():
    """
    get_gamblers() should return the list of gamblers
    associated with the dealer
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    dealer.bids = [bid]
    assert dealer.get_gamblers() == [gambler]


