import ipdb

from src.jackpot import Gambler, Dealer, Bid

if __name__=="__main__":
    
    print("hello world!!")

    gambler=Gambler("Mike")
    dealer=Dealer("Steve")
    bid=Bid(Gambler,Dealer,500)

    ipdb.set_trace()

