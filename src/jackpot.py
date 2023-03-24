class Gambler:

    all=[]

    def __init__(self, name):
        self.name=name
        self.bids=[]
        Gambler.all.append(self)

    def get_name(self):
        return self.name

    def get_bids(self):
        return self.bids

    def get_dealers(self):
        return [bid.get_dealer() for bid in self.bids]

    def highest_bid(self):
        high_bid=self.bids[0]
        for bid in self.bids:
            if(bid.get_amount()>high_bid.get_amount()):
                high_bid=bid
        return high_bid

    def average_bid_amount(self):
        if(len(self.bids)<=0): return 0
        return sum([bid.get_amount() for bid in self.bids])/len(self.bids)


    def has_bidded(self, dealer):
        return dealer in [bid.get_dealer() for bid in self.bids]

    def make_bid(self, dealer, amount):
       bid=Bid(self,dealer,amount)
       self.bids.append(bid)
       dealer.bids.append(bid)

    @classmethod
    def highest_average_gambler(cls):
        max_gambler=cls.all[0]
        for gambler in cls.all:
            if(gambler.average_bid_amount()>max_gambler.average_bid_amount()):
                max_gambler=gambler
        return max_gambler

class Dealer:

    def __init__(self, name):
        self.name=name
        self.bids=[]

    def get_name(self):
        return self.name

    def get_bids(self):
        return self.bids

    def get_gamblers(self):
        return [bid.get_gambler() for bid in self.bids]


class Bid:

    def __init__(self, gambler, dealer, amount):
       self.gambler=gambler
       self.dealer=dealer
       self.amount=amount

    def get_amount(self):
        return self.amount

    def get_gambler(self):
        return self.gambler

    def get_dealer(self):
        return self.dealer
    