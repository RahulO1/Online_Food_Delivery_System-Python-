import json

database = {}
cart = {}

database_file = 'database.json'
cart_file = 'cart.json'

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

database = load_data(database_file)
cart = load_data(cart_file)

def validate_name(name):
    return name.isalpha()

def signup():
    print("\n--- Signup ---")
    name = input("Enter your name: ")
    if not validate_name(name):
        print("Invalid name. Only alphabets are allowed.")
        return
    
    email = input("Enter your email: ")
    if email in database:
        print("Email already exists. Please login.")
        return
    
    password = input("Create a password: ")
    mobile = input("Enter your mobile number: ")
    if not mobile.isdigit() or len(mobile) != 10:
        print("Invalid mobile number. Must be 10 digits.")
        return
    
    database[email] = {"name": name, "password": password, "mobile": mobile}
    print("Signup successful! Please login to continue.")

def login():
    print("\n--- Login ---")
    email = input("Enter your email: ")
    if email not in database:
        print("Account does not exist. Please signup.")
        return False
    
    password = input("Enter your password: ")
    if database[email]["password"] != password:
        print("Incorrect password.")
        return False
    
    print(f"Welcome back, {database[email]['name']}!")
    return True

def add_to_cart(item_id, menu):
    if item_id in menu:
        # Check if item format is a dict or tuple
        if isinstance(menu[item_id], dict):
            item_name = menu[item_id]["item"]
            price = menu[item_id]["price"]
        else:
            item_name, price = menu[item_id]
        
        quantity = int(input(f"How many {item_name}s would you like to add? "))
        if quantity <= 0:
            print("Quantity must be a positive number.")
            return
        
        if item_name in cart:
            cart[item_name]['quantity'] += quantity
        else:
            cart[item_name] = {'price': price, 'quantity': quantity}
        
        print(f"{item_name} added to cart.")
    else:
        print("Invalid ID. Please try again.")

def view_cart():
    print("\n--- Cart ---")
    if not cart:
        print("Your cart is empty.")
        return 0
    
    total = 0
    for item, details in cart.items():
        total += details['price'] * details['quantity']
        print(f"{item} x{details['quantity']}: {details['price'] * details['quantity']} INR")
    
    print(f"Total: {total} INR")
    return total

def remove_from_cart():
    view_cart()
    item_name = input("Enter the name of the item you want to remove: ").strip()
    if item_name in cart:
        del cart[item_name]
        save_data(cart_file, cart)
        print(f"{item_name} removed from cart.")
    else:
        print("Item not found in cart.")

def update_cart():
    view_cart()
    item_name = input("Enter the name of the item you want to update: ").strip()
    if item_name in cart:
        try:
            quantity = int(input("Enter new quantity: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive number.")
                return
            cart[item_name]['quantity'] = quantity
            save_data(cart_file, cart)
            print(f"{item_name} quantity updated to {quantity}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Item not found in cart.")

def payment():
    total = view_cart()
    if not total:
        return
    print("\n--- Payment ---")
    print("1. Cash on Delivery (COD)")
    print("2. Card Payment")
    choice = input("Select payment method: ")
    
    if choice == '1':
        print("Order placed successfully! Pay the amount upon delivery.")
    elif choice == '2':
        card_number = input("Enter your card number: ")
        cvv = input("Enter CVV: ")
        print("Payment successful! Order placed.")
    else:
        print("Invalid payment option.")
        
    cart.clear()
    save_data(cart_file, cart)

def rating():
    print("\n\n*** Welcome to Food Rating Page ***")
    as_food = int(input("Enter number of stars for the Food (1-5): "))
    if as_food == 5:
        print("Thank you for the Five Star Rating!")
    elif as_food == 4:
        print("Thank you for the Four Star Rating!")
    else:
        print("Thank you for your Rating!")

    print("\n\n*** Welcome to Hotel Rating Page ***")
    as_hotel = int(input("Enter number of stars for the Hotel (1-5): "))
    if as_hotel == 5:
        print("Thank you for the Five Star Rating!")
    elif as_hotel == 4:
        print("Thank you for the Four Star Rating!")
    else:
        print("Thank you for your Rating!")

# Menu for Mandi Restaurant
def display_menu1():
    print("\t\t**********MANDI RESTAURANT**********")
    print("Id\tItem\t\t\tType\t\tPrice")
    print("---------------------------------------------------------------------------------------------")
    print("\t<==========================Non-Veg Items==========================>")
    print("101\tFried Mandi\t\tChicken\t\t399")
    print("102\tFaham Mandi\t\tChicken\t\t499")
    print("103\tJuicy Mandi\t\tChicken\t\t599")
    print("104\tTandoori Mandi\t\tChicken\t\t699")
    print("105\tMixed Mandi\t\tChicken\t\t799")
    print("\t<==========================Mutton Items==========================>")
    print("111\tFried Mandi\t\tMutton\t\t599")
    print("112\tFaham Mandi\t\tMutton\t\t699")
    print("113\tJuicy Mandi\t\tMutton\t\t799")
    print("114\tTandoori Mandi\t\tMutton\t\t899")
    print("115\tMixed Mandi\t\tMutton\t\t999")
    print("---------------------------------------------------------------------------------------------")
    
    menu1 = {
        101: ("Fried Mandi (Chicken)", 399),
        102: ("Faham Mandi (Chicken)", 499),
        103: ("Juicy Mandi (Chicken)", 599),
        104: ("Tandoori Mandi (Chicken)", 699),
        105: ("Mixed Mandi (Chicken)", 799),
        111: ("Fried Mandi (Mutton)", 599),
        112: ("Faham Mandi (Mutton)", 699),
        113: ("Juicy Mandi (Mutton)", 799),
        114: ("Tandoori Mandi (Mutton)", 899),
        115: ("Mixed Mandi (Mutton)", 999)
    }
    ch='y'
    while ch.lower()=='y':
        id = int(input("Enter the ID of the item you want to add to cart (or 0 to quit): "))
        add_to_cart(id,menu1)
        ch=input("Do you want to add another item press 'y' for yes 'n' for no: ")
        

# Menu for Haritha Hotel
def display_menu2():
    print("**********HARITHA HOTEL**********")
    print("Id      Item          Type        Price")
    print("---------------------------------------------------------------------------------------------")
    print("<==========================Non-Veg Items==========================>")
    print("201    Biryani         Chicken     399")
    print("202    Biryani         Mutton      499")
    print("203    Lollipop        Chicken     599")
    print("204    Wings           Chicken     699")
    print("205    KFC             Chicken     799")
    print("<=========================Veg Items===========================>")
    print("206    Dal Rice        Veg         599")
    print("207    Lemon Rice      Veg         699")
    print("208    Chapathi        Veg         799")
    print("209    Noodles         Veg         899")
    print("210    Manchuriya      Veg         999")
    print("--------------------------------------------------------------------------------------------")

    menu2 = {
        201: {"item": "Biryani", "type": "Chicken", "price": 399},
        202: {"item": "Biryani", "type": "Mutton", "price": 499},
        203: {"item": "Lollipop", "type": "Chicken", "price": 599},
        204: {"item": "Wings", "type": "Chicken", "price": 699},
        205: {"item": "KFC", "type": "Chicken", "price": 799},
        206: {"item": "Dal Rice", "type": "Veg", "price": 599},
        207: {"item": "Lemon Rice", "type": "Veg", "price": 699},
        208: {"item": "Chapathi", "type": "Veg", "price": 799},
        209: {"item": "Noodles", "type": "Veg", "price": 899},
        210: {"item": "Manchuriya", "type": "Veg", "price": 999},
    }
    ch='y'
    while ch.lower()=='y':
        id = int(input("Enter the ID of the item you want to add to cart (or 0 to quit): "))
        add_to_cart(id,menu2)
        ch=input("Do you want to add another item press 'y' for yes 'n' for no: ")

# Menu for Rice Fusion
def display_menu3():
    print("\t\t**********Rice Fusion**********")
    print("Id\tItem\t\t\tType\t\tPrice")
    print("---------------------------------------------------------------------------------------------")
    print("\t<==========================Non-Veg Items==========================>")
    print("101\tFried Rice\t\tChicken\t\t299")
    print("102\tFried Rice\t\tPrawn\t\t399")
    print("103\tChicken Curry\t\tChicken\t\t499")
    print("104\tGrilled Chicken\t\tChicken\t\t599")
    print("105\tChicken Tikka\t\tChicken\t\t699")
    print("\t<==========================Veg Items===========================>")
    print("106\tVeg Biryani\t\tVeg\t\t499")
    print("107\tVegetable Pulao\t\tVeg\t\t599")
    print("108\tPaneer Masala\t\tVeg\t\t699")
    print("109\tVegetable Noodles\tVeg\t\t799")
    print("110\tVeg Manchurian\t\tVeg\t\t899")
    print("---------------------------------------------------------------------------------------------")

    menu3 = {
        101: ("Fried Rice (Chicken)", 299),
        102: ("Fried Rice (Prawn)", 399),
        103: ("Chicken Curry", 499),
        104: ("Grilled Chicken", 599),
        105: ("Chicken Tikka", 699),
        106: ("Veg Biryani", 499),
        107: ("Vegetable Pulao", 599),
        108: ("Paneer Masala", 699),
        109: ("Vegetable Noodles", 799),
        110: ("Veg Manchurian", 899)
    }
    ch='y'
    while ch.lower()=='y':
        id = int(input("Enter the ID of the item you want to add to cart (or 0 to quit): "))
        add_to_cart(id,menu3)
        ch=input("Do you want to add another item press 'y' for yes 'n' for no: ")


# Menu for Badsha Milkshake
def display_menu4():
    print("\t\t**********Badsha Milkshake**********")
    print("Id\tItem\t\t\t\tType\t\tPrice")
    print("---------------------------------------------------------------------------------------------")
    print("<========================Milkshake Items========================>")
    print("401\tClassic Vanilla\t\tMilkshake\t149")
    print("402\tChocolate Fudge\t\tMilkshake\t199")
    print("403\tStrawberry Banana\tMilkshake\t249")
    print("404\tCookies and Cream\tMilkshake\t299")
    print("405\tSalted Caramel\t\tMilkshake\t349")
    print("406\tPeanut Butter\t\tMilkshake\t399")
    print("407\tMint Chocolate Chip\tMilkshake\t449")
    print("408\tCoffee\t\t\tMilkshake\t499")
    print("409\tNutella\t\t\tMilkshake\t549")
    print("410\tBerry Blast\t\tMilkshake\t599")
    print("---------------------------------------------------------------------------------------------")
    
    menu4 = {
        401: ("Classic Vanilla", 149),
        402: ("Chocolate Fudge", 199),
        403: ("Strawberry Banana", 249),
        404: ("Cookies and Cream", 299),
        405: ("Salted Caramel", 349),
        406: ("Peanut Butter", 399),
        407: ("Mint Chocolate Chip", 449),
        408: ("Coffee", 499),
        409: ("Nutella", 549),
        410: ("Berry Blast", 599),
    }
    ch='y'
    while ch.lower()=='y':
        id = int(input("Enter the ID of the item you want to add to cart (or 0 to quit): "))
        add_to_cart(id,menu4)
        ch=input("Do you want to add another item press 'y' for yes 'n' for no: ")


# Menu for Ram ki Bandi
def display_menu5():
    print("\t\t**********Ram ki Bandi**********")
    print("Id\tItem\t\t\tType\tPrice")
    print("---------------------------------------------------------------------------------------------")
    print("<=========================Veg Items===========================>")
    print("501\tPanner Dosa\t\tVeg\t99")
    print("502\tButter Dosa\t\tVeg\t69")
    print("503\tCheese Dosa\t\tVeg\t69")
    print("504\tSambar Idli\t\tVeg\t59")
    print("505\tSambar Vada\t\tVeg\t59")
    print("506\tIdli\t\t\tVeg\t49")
    print("507\tDosa\t\t\tVeg\t79")
    print("508\tPuri\t\t\tVeg\t69")
    print("509\tVada\t\t\tVeg\t59")
    print("510\tUpma\t\t\tVeg\t89")
    print("511\tMasala Dosa\t\tVeg\t99")
    print("512\tMasala Vada\t\tVeg\t79")
    print("513\tBonda\t\t\tVeg\t69")
    print("514\tBajji\t\t\tVeg\t79")
    print("515\tUttapam\t\t\tVeg\t99")
    print("516\tPongal\t\t\tVeg\t89")
    print("517\tVegetable Pulao\t\tVeg\t129")
    print("518\tAloo Paratha\t\tVeg\t119")
    print("519\tGobi Paratha\t\tVeg\t119")
    print("520\tPaneer Paratha\t\tVeg\t139")
    print("521\tTomato Rice\t\tVeg\t99")
    print("522\tLemon Rice\t\tVeg\t89")
    print("523\tCurd Rice\t\tVeg\t79")
    print("524\tBisibele Bath\t\tVeg\t109")
    print("525\tVeg Pulao\t\tVeg\t129")
    print("526\tVegetable Biryani\tVeg\t149")
    print("527\tVegetable Fried Rice\tVeg\t119")
    print("528\tPongal with Chutney\tVeg\t99")
    print("529\tKhichdi\t\t\tVeg\t109")
    print("530\tVegetable Khichdi\tVeg\t119")
    print("---------------------------------------------------------------------------------------------")

    menu5 = {
        501: ("Panner Dosa", 99),
        502: ("Butter Dosa", 69),
        503: ("Cheese Dosa", 69),
        504: ("Sambar Idli", 59),
        505: ("Sambar Vada", 59),
        506: ("Idli", 49),
        507: ("Dosa", 79),
        508: ("Puri", 69),
        509: ("Vada", 59),
        510: ("Upma", 89),
        511: ("Masala Dosa", 99),
        512: ("Masala Vada", 79),
        513: ("Bonda", 69),
        514: ("Bajji", 79),
        515: ("Uttapam", 99),
        516: ("Pongal", 89),
        517: ("Vegetable Pulao", 129),
        518: ("Aloo Paratha", 119),
        519: ("Gobi Paratha", 119),
        520: ("Paneer Paratha", 139),
        521: ("Tomato Rice", 99),
        522: ("Lemon Rice", 89),
        523: ("Curd Rice", 79),
        524: ("Bisibele Bath", 109),
        525: ("Veg Pulao", 129),
        526: ("Vegetable Biryani", 149),
        527: ("Vegetable Fried Rice", 119),
        528: ("Pongal with Chutney", 99),
        529: ("Khichdi", 109),
        530: ("Vegetable Khichdi", 119)
    }
    ch='y'
    while ch.lower()=='y':
        id = int(input("Enter the ID of the item you want to add to cart (or 0 to quit): "))
        add_to_cart(id,menu5)
        ch=input("Do you want to add another item press 'y' for yes 'n' for no: ")

def choose_favorite_restaurant():
    print("1. Mandi Restaurant")
    print("2. Haritha Hotel")
    print("3. Rice Fusion")
    print("4. Badsha Milkshake")
    print("5. Ram ki Bandi")
    
    try:
        choice = int(input("Enter your favorite restaurant (choose a number): "))
        if choice == 1:
            print("You chose: Mandi Restaurant")
            display_menu1()
        elif choice == 2:
            print("You chose: Haritha Hotel")
            display_menu2()
        elif choice == 3:
            print("You chose: Rice Fusion")
            display_menu3()
        elif choice == 4:
            print("You chose: Badsha Milkshake")
            display_menu4()
        elif choice == 5:
            print("You chose: Ram ki Bandi")
            display_menu5()
        else:
            print("Invalid choice. Please select a number from 1 to 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n--- Online Food Ordering System ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            signup()
        elif choice == '2':
            if login():
                while True:
                    print("\n1. View Restaurants")
                    print("2. View Cart")
                    print("3. Update Cart")
                    print("4. Remove From Cart")
                    print("5. Make Payment")
                    print("6. Rating for Food and the Hotel")
                    print("7. Logout")

                    user_choice = input("Enter your choice: ")
                    
                    if user_choice == '1':
                        choose_favorite_restaurant()
                    elif user_choice == '2':
                        view_cart()
                    elif user_choice == '3':
                        update_cart()
                    elif user_choice == '4':
                        remove_from_cart()
                    elif user_choice == '5':
                        payment()
                    elif user_choice == '6':
                        rating()
                    elif user_choice == '7':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Thank you for using the Online Food Ordering System!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
