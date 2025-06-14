import art
information = {}
addMore = True

while addMore:
    print(art.logo)
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: "))
    information[name] = bid
    yN = input("Do you want to add more bids? Type 'yes' or 'no'\n")
    if yN == "no":
        addMore = False
    else:
        print("\n" * 100)

maxBid = ["name", 0]
for key in information:
    if information[key] > maxBid[1]:
        maxBid[0] = key
        maxBid[1] = information[key]

print("\n" *100)
print(art.logo)
print(f"The highest bidder was {maxBid[0]} with a bid of {maxBid[1]}")