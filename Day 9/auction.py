import art

# 1 add logo at the start
print(art.logo)

# 2 create an empty dictionary to hold names and bid values

bids = {}
# 3 ask for name and bid
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? : ")
    price = input("What is your bid? : £ ")
    # 5 add the name and bid to the empty dictionary
    bids[name] = price
    should_conitue = input("Are there any other bidders? Tpye yes/no: ")
    # 6 ask if there is another bid
    if should_conitue == "no":
        bidding_finished = True
    elif should_conitue == "yes":
        clear


# 7 if yes clear screen and repeat steps 2 5

# of no check all the bids and print out the highest bidder's name.
