import os
os.system("cls")

#Get product purchase information from the user (1)
customerName = input("Customer name: ")
productName = input("Product name: ")
quantity = int(input("Quantity purchased: "))
price = float(input("Price: "))

#validate responses, calculate price
if quantity > 0 and price > 0:
    totalPrice = price * quantity
    adjPrice = round(totalPrice, 2)
    #print final total
    print(f"Customer {customerName} purchased {quantity} {productName}s for ${adjPrice}.")
else:
    print("Invalid input. Please try again.")

#check if user wants to continue
choice = input("Do you want to generate another receipt? (y/n) ")
if choice.lower() == "y":
    customerName = input("Customer name: ")
    productName = input("Product name: ")
    quantity = int(input("Quantity purchased: "))
    price = float(input("Price: "))

    #validate responses, calculate price
    if quantity > 0 and price > 0:
        totalPrice = price * quantity
        adjPrice = round(totalPrice, 2)
        #print final total
        print(f"Customer {customerName} purchased {quantity} {productName}s for ${adjPrice}.")
    else:
        print("Invalid input. Please try again.")
else:
    print("Finished")
