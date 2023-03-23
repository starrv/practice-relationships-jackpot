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
        max_bid=self.bids[0]
        for i in range(1,len(self.bids)):
            if(self.bids[i].get_amount()>max_bid.get_amount()):
                max_bid=self.bids[i]
        return max_bid
        
        
        """h=0
        max_bid=None
        for bid in self.get_bids():
            if(bid.get_amount()>h):
                h=bid.amount
                max_bid=bid
        return max_bid
    
        return max(self.bids,key=lambda bid: bid.amount)
        """
        

    def average_bid_amount(self):
        total_amount=sum(bid.get_amount() for bid in self.bids)
        if(len(self.bids)<=0):
            return 0
        return total_amount/len(self.bids)

    def has_bidded(self, dealer):
        dealer in [bid.get_dealer() for bid in self.bids if bid.get_dealer()==dealer]

    def make_bid(self, dealer, amount):
       bid=Bid(self,dealer,amount)
       self.bids.append(bid)

    @classmethod
    def highest_average_gambler(cls):
        high_roller=cls.all[0]
        for gambler in cls.all:
            if(gambler.average_bid_amount()>high_roller.average_bid_amount()):
                high_roller=gambler
        return high_roller


        highest_gambler=None
        for gambler in cls.all:
            average_bid=gambler.average_bid_amount()
            if(average_bid>highest_average_bid):
                highest_gambler=gambler
                highest_average_bid=average_bid
        return highest_gambler

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
        pass

    def get_gambler(self):
        pass

    def get_dealer(self):
        return self.dealer
    