# Shopping Cart System 
# Diane Hsieh 
# AM 

# python module for time
from datetime import date 

# list for products 
products = ["Chips", "Soda" "Candy", "Cookies", "Water", "Sandwich"]

# list for prices 
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

# empty list for shopping cart 
shopping_cart = [] 

print() 
print() 

print(" ========== SMART SHOPPING CART ========== ")    
print("1. View Available Products")
print("2. Add Product to Cart")
print("3. Remove Product from Cart")
print("4. View Shopping Cart")
print("5. View Current Total")
print("6. Checkout")

choice = int(input("Enter your choice: "))

while choice != 6: 

# customer chooses option 1 : view available products 
    if choice == 1: 
        print(" ======== AVAILABLE PRODUCTS ======== ")
        for item in products:
            for i in prices: 
                print (products[index,item],".", item, i)

    # customer chooses option 2: add product to cart 
    if choice == 2: 
        print("Which product would you like to add?")
        for item in products: 
            print(item)
        chosen = input("Enter product number: ")

        # to validate that product number exists 
        while (chosen != 1) or (chosen != 2) or (chosen != 3) or (chosen != 4) or (chosen != 5) or (chosen != 6): 
            print("Invalid product!")
            print("Please choose a number between 1 and 6. ")
            chosen = input("Enter product number: ")

        print(chosen, "was added to your cart!")
        # added to cart
        # ask if i can use "insert" instead of "append"
        shopping_cart.insert(0, products[chosen - 1])

    # customer chooses option 3: remove product from cart 
    if choice == 3:
        print(" ======== YOUR SHOPPING CART ======== ")

        if shopping_cart == []:
            print("Your shopping cart is empty!")
            print("There is nothing to remove.")
        else:
            # displaying the current shopping cart
            for item in shopping_cart:
                print(item)
            print("Which item would you like to remove?")
            remove = input("Enter the item number: ")
        
            # validate that the item number exists in the cart

    # customer chooses option 4: view shopping cart
    if choice == 4:
        print(" ======== YOUR SHOPPING CART ======== ")
        if shopping_cart == []:
            print("Your shopping cart is empty!")
        else:
            for item in shopping_cart:
                for i in prices:
                    print(item, i)
                    print("Total Items:", len(shopping_cart))

    # customer chooses option 5: view current total
    if choice == 5: 
        print(" ======== CURRENT TOTAL ======== ")
        subtotal = 0
        for item in shopping_cart:
            subtotal = subtotal + prices[products.index(item)]
        print("Subtotal: $", subtotal)

    print() 
    print() 
    
    print(" ========== SMART SHOPPING CART ========== ")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    
    choice = int(input("Enter your choice: "))

# customer chooses option 6: checkout
if choice == 6:
    print(" ======== CHECKOUT ======== ")

    subtotal = 0
    for item in shopping_cart:
        subtotal = subtotal + prices[products.index(item)]
    
    # function to calculate discount
    def calculate_discount(subtotal):
        discount = 0 
        # if statement to see if customer can get discount based on subtotal
        if subtotal >= 40: 
            discount = subtotal * 0.15 
        elif subtotal >= 20: 
            discount = subtotal * 0.10
        elif subtotal >= 10:
            discount = subtotal * 0.05
        elif subtotal == 0: 
            discount = 0
        else: 
            discount = 0
        return discount

    # final cost 
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount

    # checkout page 

    print("Date:", date.today())
    print("Subtotal: $", subtotal)
    print("Discount:", (subtotal - discount), "%")
    print("Amount saved: $", discount)

    print() 

    print("Final Total: $", final_total)

    print() 

    print("Thank you for shopping!")