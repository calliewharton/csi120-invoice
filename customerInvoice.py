import os
os.system("cls")

#Get product purchase information from the user (1)
customerName = input("Customer name: ")
productName = input("Product name: ")
quantity = int(input("Quantity purchased: "))
price = float(input("Price: "))

#calculate total price 
totalPrice = price * quantity
adjPrice = round(totalPrice, 2)

#print final total
print(f"Customer {customerName} purchased {quantity} {productName}s for ${adjPrice}.")

#check if user wants to continue
choice = input("Do you want to generate another receipt? (y/n) ")
if choice.lower() == "y":
    customerName = input("Customer name: ")
    productName = input("Product name: ")
    quantity = int(input("Quantity purchased: "))
    price = float(input("Price: "))

    totalPrice = price * quantity
    adjPrice = round(totalPrice, 2)
    print(f"Customer {customerName} purchased {quantity} {productName}s for ${adjPrice}.")
else:
    print("Finished")
