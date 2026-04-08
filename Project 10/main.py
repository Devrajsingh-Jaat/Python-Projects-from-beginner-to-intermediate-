import art

# TODO-1: Ask the user for input
auction_running = True
auction_people = {}
highest_bidder_name = ""
highest_bid = 0

print(art.logo)
print("Welcome to the Auction Project!")

# TODO-2: Save data into dictionary {name: price}
while auction_running:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    auction_people[name] = bid
    should_continue = input("Are there any other bidders? Yes or No: ").lower()

    if should_continue == "no":
        auction_running = False
    elif should_continue == "yes":
        print("\n" * 100)
    else:
        print("Please enter yes or no")

# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary
for key in auction_people:
    if auction_people[key] > highest_bid:
        highest_bidder_name = key
        highest_bid = auction_people[key]

print("\n" * 100)
print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}!")


