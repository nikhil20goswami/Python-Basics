cost_price = int(input("Enter the cost price :"))
selling_price = int(input("Enter the selling price :"))

if selling_price>cost_price:
    profit = selling_price-cost_price
    print("We made profit of : ",profit)

elif selling_price<cost_price:
    loss = cost_price-selling_price
    print("We have incured loss of :",loss)

else:
    print("We have no loss and no profit")
