# Question B12: WAP to input the selling price and cost price
#  from the user and determine whether the seller has made profit
# or incurred loss. Also display the value of profit or loss.
buying = int(input("Buying cost: "))
selling = int(input("Selling cost: "))
if(buying>selling):
    print("loss of Rs.",buying-selling)
else:
    print("Profit of Rs.",selling-buying)