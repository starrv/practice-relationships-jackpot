from src.jackpot import Gambler, Bid, Dealer


def test_gambler_init_name():
    """
    Should be able to initialize a gambler object
    with a name
    """
    gambler = Gambler("Mike")
    assert gambler.name == "Mike"

def test_gambler_get_name():
    """
    get_name() should return the name of the gambler
    """
    gambler = Gambler("Mike")
    assert gambler.get_name() == "Mike"

def test_gambler_get_bids():
    """
    get_bids() should return the list of bids
    associated with the gambler
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    gambler.bids = [bid]
    assert gambler.get_bids() == [bid]

def test_gambler_get_dealers():
    """
    get_dealers() should return the list of dealers
    associated with the gambler
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    gambler.bids = [bid]
    assert gambler.get_dealers() == [dealer]

def test_gambler_average_bid_amount():
    """
    average_bid_amount() should return the average 
    bid amount for the gambler
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    gambler.bids = [bid]
    assert gambler.average_bid_amount() == 500

def test_gambler_highest_bid():
    """
    highest_bid() should return the object
    with the highest bid amount for the gambler
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid_high = Bid(gambler, dealer, 500)
    bid_low = Bid(gambler, dealer, 100)
    gambler.bids = [bid_high, bid_low]
    assert gambler.highest_bid() == bid_high

def test_gambler_make_bid():
    """
    make_bid(dealer, amount) should create a new bid
    object and attach it to the gambler
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    gambler.make_bid(dealer, 500)
    assert len(gambler.bids) == 1
    assert gambler.bids[0].amount == 500

def test_gambler_has_bidded():
    """
    has_bidded(dealer) should return True if the
    gambler has made a bid with this deal, False otherwise
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    gambler.bids = [bid]
    assert gambler.has_bidded(dealer) == True

def test_shows_highest_average_gambler():
    '''has a class method "highest_average_gambler" that returns the gambler with the highest average bids.'''
    dealer_1 = Dealer('Steve')
    dealer_2 = Dealer('Tom')
    dealer_3 = Dealer('Joe')
    
    Gambler.all = []
    
    gambler_1 = Gambler(name="Mike")
    gambler_1.bids = [Bid(gambler_1,dealer_1,500),Bid(gambler_1,dealer_2,1000)]
    Gambler.all.append(gambler_1)
    
    gambler_2 = Gambler(name="Sam")
    gambler_2.bids = [Bid(gambler_2,dealer_1,100),Bid(gambler_1,dealer_2,200)]
    Gambler.all.append(gambler_2)

    assert Gambler.highest_average_gambler() == gambler_1
