# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

def highest_bid(bid_status):
    winning_bid = 0
    winner = ""
    for bidder in bid_status:
        bid_price = bid_status[bidder]
        if bid_price >  winning_bid:
            winning_bid = bid_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${winning_bid}")

bidders = {}
auction_status = True
while auction_status:
    name = input("What is your name?")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    status = input("Are there any other bidders? type yes or no\n").lower()
    if status == "no":
        auction_status = False
        highest_bid(bidders)
    elif status == "yes":
        print("\n" * 20)



