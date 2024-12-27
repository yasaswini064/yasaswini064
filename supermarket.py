name = input("Enter your Name: ")

# List of items
items_list = '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
'''

# Prices for items
item_rates = {
    'rice': 10, 'sugar': 8, 'oil': 30, 'salt': 25
}

# Initialize variables
total_price = 0
pricelist = []

while True:
    option = input("Press 1 for item list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping!")
        break
    elif option == '1':
        print(items_list)

        while True:
            choice = input("Press 1 to buy items or 2 to stop shopping: ")
            if choice == '2':
                print("Thank you for shopping!")
                break
            elif choice == '1':
                item = input("Enter the item name: ").lower()
                if item in item_rates:
                    while True:
                        quantity = input("Enter quantity: ")
                        if quantity.isdigit():
                            quantity = int(quantity)
                            break
                        else:
                            print("Please enter a valid quantity.")

                    price = item_rates[item] * quantity
                    pricelist.append((item, quantity, price))
                    total_price += price
                else:
                    print("Sorry, the selected item is not available.")

        if total_price > 0:
            tax = total_price * 0.12
            final_amount = total_price + tax

            print("\n================== Amma Supermarket ==================")
            print("Location: Vijayawada")
            print("Customer Name:", name)
            print("---------------------------------------------------------")
            print(f"{'S.No':<5} {'Item':<10} {'Quantity':<10} {'Price':<10}")

            for i in range(len(pricelist)):
                print(f"{i+1:<5} {pricelist[i][0]:<10} {pricelist[i][1]:<10} Rs {pricelist[i][2]:<10}")
            print("---------------------------------------------------------")
            print(f"{'Total Amount:':<40} Rs {total_price:.2f}")
            print(f"{'Tax (12%):':<40} Rs {tax:.2f}")
            print(f"{'Final Amount:':<40} Rs {final_amount:.2f}")
            print("---------------------------------------------------------")
            print("Thank you for shopping with us! Visit again.")
            print("=========================================================")
