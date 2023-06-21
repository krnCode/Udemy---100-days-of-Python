import art

print(art.logo)

print("Welcome to the secret auction program.")

bidders = []
auction = True


def bidders_bids(bidder, bid):
    new_bidder = {}
    new_bidder["Bidder Name"] = bidder
    new_bidder["Bid Value"] = bid
    bidders.append(new_bidder)


def winning_bid():
    for bidder in bidders:
        max_value = 0
        max_bidder = {}
        if bidder["Bid Value"] > max_value:
            max_value = bidder["Bid Value"]
            max_bidder = bidder
        else:
            max_value = max_value

    print(
        f"The winner is {max_bidder['Bidder Name']} with a bid of ${max_bidder['Bid Value']}"
    )


while auction:
    enter_bidder = input("What is your name? ")
    enter_bid = int(input("What's your bid? $"))

    bidders_bids(enter_bidder, enter_bid)

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if more_bidders != "yes":
        winning_bid()
        auction = False
