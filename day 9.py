# Day 9
# Auction project


# auction= {
    
# }


# def getAddBidder(name,bid): 
#         diction={}
#         diction["Name"]=name,
#         diction["Bid"]=bid
#         # print(diction)
#         for key in diction:
#                 print(diction[key])
                
#                    # print(diction)     



# getAddBidder("Desire",10)
# getAddBidder("Patrick",50)
# getAddBidder("eric",30)

# print(auction)





# import clear

print ("Welcome to the awesome Auction")

bids ={}

bidding_finished = False


while not bidding_finished:
    name= input("What is your name?")
    price= int(input("What is your bid? $"))
    bids[name]= price
    Answer= input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    if Answer=='no':
        print(bids)
        bidding_finished = True
        highest= 0
        winner =''
        for key in bids:            
            if bids[key] > highest:
                highest= bids[key]
                winner=key
        print(f"highest bid is {winner} with {highest}")
         
    elif Answer =='yes':
        bidding_finished=False
    else:
        bidding_finished = False
        print("Type correct yes or no, it means you want still to bid")
    
