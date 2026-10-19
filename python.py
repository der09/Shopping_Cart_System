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

while choice < 1 or choice > 6:
    print("Invalid")
    print("Please choose a number 1 and 6.")
    print() 
    choice = int(input("Enter your choice: "))
    print()

def avaliable_products(): 
# customer chooses option 1 : view available products 
    print(" ======== AVAILABLE PRODUCTS ======== ")
    for item in products:
        for i in prices: 
            print (products[item],".", item, i)

def add_product():
    # customer chooses option 2: add product to cart 
    print("Which product would you like to add?")
    for item in range(len(products)): 
        print(item + 1, ".", products[item])
    chosen = int(input("Enter product number: "))

    # to validate that product number exists 
    while (chosen < 1 or chosen > 6):
        print("Invalid product!")
        print("Please choose a number between 1 and 6. ")
        chosen = int(input("Enter product number: "))

    print(chosen, "was added to your cart!")
    # added to cart
    shopping_cart.append(products[chosen - 1])
    print(products[chosen - 1], "was added to your cart!")


def remove_product():
# customer chooses option 3: remove product from cart 
    
    print(" ======== YOUR SHOPPING CART ======== ")

    if shopping_cart == []:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
    else:
        # displaying the current shopping cart
        for item in range(len(shopping_cart)):
            print(item + 1, ".", shopping_cart[item])
        print("Which item would you like to remove?")
        remove = int(input("Enter the item number: "))
    
        # validate that the item number exists in the cart
        while (remove < 1 or remove > len(shopping_cart)):
            print("Invalid item number!")
            print("Please choose a number between 1 and", len(shopping_cart))
            remove = int(input("Enter the item number: "))

        # removes item from cart 
        shopping_cart.pop[remove - 1]
        print(shopping_cart[remove - 1], "was removed from your cart!")

def view_cart():
    # customer chooses option 4: view shopping cart
        print(" ======== YOUR SHOPPING CART ======== ")
        if shopping_cart == []:
            print("Your shopping cart is empty!")
        else:
            for item in range(len(shopping_cart)):
                print(item + 1, ".", shopping_cart[item], "$", f"{prices[products.index(shopping_cart[item])]:.2f}")
            print("Total Items:", len(shopping_cart))


def view_total():
    # customer chooses option 5: view current total
    print(" ======== CURRENT TOTAL ======== ")
    subtotal = 0
    for item in range(len(shopping_cart)):
        subtotal = subtotal + prices[products.index(shopping_cart[item])]
    print("Subtotal: $", subtotal)


def menu():
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
    return choice 

# while loop 
while choice !=6: 
    if choice == 1 : 
        avaliable_products()
        choice = menu()
    elif choice == 2: 
        add_product() 
        choice = menu() 
    elif choice == 3: 
        remove_product() 
        choice = menu()
    elif choice == 4: 
        view_cart() 
        choice = menu() 
    elif choice == 5: 
        view_total() 
        choice = menu()
    

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

# customer chooses option 6: checkout
if choice == 6:
    print(" ======== CHECKOUT ======== ")

    subtotal = 0
    for item in shopping_cart:
        subtotal = subtotal + prices[products.index(item)]

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