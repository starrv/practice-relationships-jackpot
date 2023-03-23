from src.jackpot import Gambler, Bid, Dealer


def test_bid_init_gambler_dealer_amount():
    """
    Should be able to initialize a bid object with
    a gambler, dealer, and amount
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    assert bid.amount == 500
    assert bid.dealer == dealer
    assert bid.gambler == gambler

def test_bid_get_amount():
    """
    get_amount() should return the amount for the bid
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    assert bid.amount == 500

def test_bid_get_gambler():
    """
    get_gambler() should return the gambler associated
    with the bid
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    assert bid.get_gambler() == gambler

def test_bid_get_dealer():
    """
    get_dealer() should return the movie associated
    with the review
    """
    gambler = Gambler("Mike")
    dealer = Dealer('Steve')
    bid = Bid(gambler, dealer, 500)
    assert bid.get_dealer() == dealer
