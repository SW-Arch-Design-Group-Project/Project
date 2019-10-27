import login
import createdatabase
import sqlite3
import time

def main():

    #Builds initial Database.
    createdatabase.buildDatabase()

    print("\n***************************")
    print("*  Welcome to the Store!  *")
    print("***************************\n")
    print("All items have been Restocked!\n\n")

    # login and validation (if it doesn't return a boolean, change this to accept a username.)
    userLogin()

def userLogin():
    userID = login.ValidateUser()
    session = homeScreen(userID)
    return



def homeScreen(userID):
    currentUser = userID
    conn = sqlite3.connect('store.db')
    exitStore = 0

    while (exitStore != 1):
        try:
            print("\n---------------- Store Home ----------------")
            print("Store Options:\n1. View Inventory\n2. View Past Orders\n3. Build Cart\n9. Logout\n0. Exit Store\n")
            userSelection = int(input("Select an option: "))

            if (userSelection) == (1):
                displayTable(conn)
            if (userSelection) == (2):
                displayOrderHistory(conn, currentUser)
            if (userSelection) == (3):
                addToCart(conn, currentUser)
            if (userSelection) == (9):
                print("\n**********************************")
                print("*  Thanks for Shopping with us!  *")
                print("**********************************\n\n\n")
                userLogin()
            if (userSelection) == (0):
                print("\n**********************************")
                print("*  Thanks for Shopping with us!  *")
                print("**********************************\n")
                exit()

        except Exception as ex:
            print("Please enter a store option.\n")

    return conn


def displayOrderHistory(conn, currentUser):
    print("\n---------------- Order History ----------------")

    cursor = conn.execute("SELECT UserID FROM User WHERE Username = ?", (currentUser,))
    data = cursor.fetchone()
    if (data is None):
        print("You are not a user")

    else:
        userID = data[0]
        hasOrders = True

        cursor = conn.execute("SELECT * FROM PurchaseHistory WHERE UserID = ?", (userID,))
        data = cursor.fetchone()

        if (data is None):
            print("You have no previous orders.\n")
            hasOrders = False

        else:
            print('{:<10s}{:>25s}{:>30s}{:>35s}{:>45s}'.format("\nPurchase ID", "Order ID", "User ID",
                                                               "Total", "Credit Card"))

        while (hasOrders == True):
            print('{:<10d}{:>25d}{:>30d}{:>35.2f}{:>45d}'.format(data[0], data[1], data[2],
                  data[3], data[4]))
            data = cursor.fetchone()
            if (data is None):
                break




def displayTable(conn):
    print("\n---------------- Store Inventory ----------------")


    # TODO Add this function that will display the items from the Database that will be available
    #      add to cart.
    cursor = conn.execute('SELECT * FROM Inventory')

    print('{:<10s}{:<15s}{:<20s}{:<25s}{:<30s}{:<35s}'.format("\nItem ID", "Name", "Quantity",
                                                              "Price","Category", "Desc"))

    for row in cursor:
        print('{:<10d}{:<15s}{:<20d}{:<25.2f}{:<30s}{:<35s}'.format(row[0], row[1], row[5],
            row[3], row[4], row[2]))
    print("\n")

    return



def addToCart(conn, currentUser):

    # TODO This function will be responsible for adding an item to a shopping cart.
    print("\n---------------- Cart Builder ----------------")
    cart = []
    still_shopping = True
    while still_shopping == True:

        itemID = int(input("Enter an Item ID to add it to your cart: "))
        quantity = int(input("Enter a quantity: "))

        cursor = conn.execute("SELECT * FROM Inventory WHERE ItemID = ? AND Quantity >= ?", (itemID, quantity,))
        data = cursor.fetchone()

        # Check if item and quantity is in stock
        if (data is None):
            print("\nThat Item is out of stock or in reduced quantity.\n")
        else:
            print('{:<10s}{:<15s}{:<25s}'.format("\nItem ID", "Name", "Price"))
            print('{:<10d}{:<15s}{:<25.2f}'.format(data[0], data[1], data[3]))
            print("Successfully Added to Cart.\n")

            # Add        itemID,  name,    quantity
            cart.append([data[0], data[1], quantity])

        # Prompt user to continue shopping
        done = str(input("Are you finished adding items? (y/n): "))
        if (done == 'y'):
            still_shopping = False
            break

    reviewCart(currentUser, conn, cart)

def reviewCart(currentUser, conn, cart):
    print("\n---------------- Review Cart ----------------")

    runningTotal = 0;
    print('{:<10s}{:<15s}{:<20s}{:<25s}{:<30s}'.format("\nItem ID", "Name", "Price", "Quantity", "Total"))

    for element in range(len(cart)):
        currentIndex = cart[element][0]
        cursor = conn.execute("SELECT * FROM Inventory WHERE ItemID = ?", (currentIndex,))
        data = cursor.fetchone()
        runningTotal = (runningTotal + (data[3] * cart[element][2]))
        print('{:<10d}{:<15s}{:<20.2f}{:<25d}{:<30.2f}'.format(data[0], data[1], data[3],
                                                               cart[element][2], (data[3] * cart[element][2])))
    # Print running total to screen

    print("---------------------------------------------------------------------------")
    print('{:>75.2f}'.format(runningTotal))

    proceedToCheckout = False
    while not proceedToCheckout:
        print("\nCart Options:\n1. Remove Item\n2. Proceed To Checkout\n3. Delete Cart")
        cartSelection = int(input("\nSelect an option: "))

        if (cartSelection == 1):
            rmItem = int(input("Enter ItemID you wish to remove: "))
            rmQuantity = int(input("Enter quantity you wish to remove: "))

            for element in range(len(cart)):
                if (cart[element][0] == rmItem) and (cart[element][2] <= rmQuantity):
                    cart.pop(element)
                    print("Item removed from your cart")
                    break
                if (cart[element][0] == rmItem) and (cart[element][2] > rmQuantity):
                    cart[element][2] = (cart[element][2] - rmQuantity)
                    print(rmQuantity, "removed from item", rmItem)
                    break
                # else:
                #     print("Item was not found in your cart")

            reviewCart(conn, cart)

        if (cartSelection == 2):
            proceedToCheckout = True
        if (cartSelection == 3):
            homeScreen()
        else:
            continue

    confirmPurchase(currentUser, cart, conn)


# allow user to confirm his/her purchase
def confirmPurchase(currentUser, cart, conn):
    print("\n---------------- Confirm Purchase ----------------")

    #Get UserID from currentUser
    cursor = conn.execute("SELECT UserID FROM User WHERE Username = ?", (currentUser,))
    data = cursor.fetchone()
    UserID = data[0]

    #Search database for user address, then prompt if not there
    cursor = conn.execute("SELECT Address FROM User WHERE UserID = ?", (UserID,))
    data = cursor.fetchone()
    if (data is None):
        address = input("\nPlease enter your address for shipment: ")
        conn.execute("INSERT INTO User WHERE UserID = ? (Address)\
            VALUES (?)", (UserID, address,));
        print("\nAddress information stored in database.\n")
    else:
        print("\nAddress information found in database.\n")
        address = data[0]

    #Get credit card info from user
    creditcard = int(input("\nPlease enter your credit card information for the purchase: "))

    #First insert into the orders table to create the orderID
    conn.execute ("INSERT INTO Orders (UserID)\
        VALUES (?)", (UserID,));

    #Select the most recent orderID for the user
    cursor = conn.execute("SELECT MAX(OrderID) FROM Orders WHERE UserID = ?", (UserID,))
    data = cursor.fetchone()
    OrderID = data[0]

    #Insert the itemID's and their quantities into the OrderItems Table and update the Inventory table
    total = 0
    for item in cart:
        price = 0
        ItemID = item[0]
        Quantity = item[2]
        cursor = conn.execute("SELECT Price FROM Inventory WHERE ItemID = ?", (ItemID,))
        data = cursor.fetchone()
        price = data[0]
        total += price * Quantity

        conn.execute("INSERT INTO OrderItems (OrderID, ItemID, Quantity)\
            VALUES (?, ?, ?)", (OrderID, ItemID, Quantity,));

        cursor = conn.execute("SELECT Quantity FROM Inventory WHERE ItemID = ?", (ItemID,))
        data = cursor.fetchone()
        current_quantity = data[0]

        new_quantity = current_quantity - Quantity
        conn.execute("UPDATE Inventory SET Quantity = ? WHERE ItemID = ?", (new_quantity,ItemID,))

    #Insert PurchaseHistory table info with calculated total
    conn.execute("INSERT INTO PurchaseHistory (OrderID, UserID, Total, CreditCard)\
            VALUES (?, ?, ?, ?)", (OrderID, UserID, total, creditcard,));

    conn.commit()

    print("\n---------------- Order Confirmed ----------------")
    print('{:<10s}{:<15s}{:<25s}{:<45s}'.format("Order ID", "Total", "Payment Method", "Sipping Address"))
    print('{:<10d}{:<15.2f}{:<25d}{:<45s}'.format(OrderID, total, creditcard, address))


# MAIN FUNCTION CALL
if __name__ == "__main__":
    main()