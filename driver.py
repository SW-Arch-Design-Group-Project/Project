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
    userID = login.ValidateUser()
    session = homeScreen(userID)


def homeScreen(userID):
    print("\n---------------- Store Home ----------------\n")
    currentUser = userID
    conn = sqlite3.connect('store.db')
    exitStore = 0

    while (exitStore != 1):
        try:
            print("Store Options:\n1. View Inventory\n2. View Past Orders\n3. Build Cart\n0. Exit Store\n")
            userSelection = int(input("Select an option: "))

            if (userSelection) == (1):
                displayTable(conn)
            if (userSelection) == (2):
                displayOrderHistory(conn, currentUser)
            if (userSelection) == (3):
                addToCart(conn, currentUser)
            if (userSelection) == (0):
                print("\n**********************************")
                print("*  Thanks for Shopping with us!  *")
                print("**********************************\n")
                exit()

        except Exception as ex:
            print("Please enter a store option.\n")

    return conn


def displayOrderHistory(conn, currentUser):
    cursor = conn.execute("SELECT UserID FROM User WHERE Username = ?", (currentUser,))
    for row in cursor:
        userID = row[0]
        print(type(userID))
    print(userID)

    cursor = conn.execute("SELECT * FROM PurchaseHistory WHERE UserID = ?", (userID,))

    print('{:<10s}{:>25s}{:>30s}{:>35s}{:>45s}'.format("\nPurchase ID", "Order ID", "User ID",
                                                       "Total", "Credit Card"))
    for row in cursor:
        print('{:<10d}{:>25d}{:>30d}{:>35.2f}{:>45d}'.format(row[0], row[1], row[2],
              row[3], row[4]))


def displayTable(conn):

    # TODO Add this function that will display the items from the Database that will be available
    #      add to cart.
    cursor = conn.execute('SELECT * FROM Inventory')

    print('{:<10s}{:<15s}{:<20s}{:<25s}{:<30s}{:<35s}'.format("\nItem ID", "Name", "Quantity",
                                                              "Price","Category", "Desc"))

    for row in cursor:
        print('{:<10d}{:<15s}{:<20d}{:<25.2f}{:<30s}{:<35s}'.format(row[0], row[1], row[5],
            row[3], row[4], row[2]))
    print("\n")

    addToCart()

    return



def addToCart(conn, currentUser):

    # TODO This function will be responsible for adding an item to a shopping cart.
    print("\n---------------- Cart Builder ----------------\n")
    cart = []
    still_shopping = True
    while still_shopping == True:

        itemID = int(input("Enter an Item ID to add it to your cart: "))
        quantity = int(input("Enter a quantity: "))

        cursor = conn.execute("SELECT * FROM Inventory WHERE ItemID = ? AND Quantity >= ?", (itemID, quantity,))
        data = cursor.fetchone()

        # Check if item and quantity is in stock
        if (data is None):
            print("That Item is out of stock or in reduced quantity.")
        else:
            print('{:<10s}{:<15s}{:<25s}'.format("\nItem ID", "Name", "Price"))
            print('{:<10d}{:<15s}{:<25.2f}'.format(data[0], data[1], data[3]))
            print("Successfully Added to Cart.\n")

            cart.append([data[0], data[1], quantity])

        # for each in cart:
        #     itemID.append(cart)
        #     for object in cart:
        #         itemQuantity.append(cart)
        # return


def confirmPurchase(UserID, cart):

    #First insert into the orders table to create the orderID
    conn.execute ("INSERT INTO Orders (UserID)\
        VALUES (?)", (UserID,));

    #Select the most recent orderID for the user
    OrderID = conn.execute("SELECT MAX(OrderID) FROM Orders WHERE UserID = ?", (UserID,))

    #Insert the itemID's and their quantities into the OrderItems Table and update the Inventory table
    total = 0
    for item in cart:
        price = 0
        ItemID = [item][0]
        Quantity = [item][1]
        price = conn.execute("SELECT Price FROM Inventory WHERE ItemID = ?", (ItemID,))
        total += price * Quantity
        conn.execute("INSERT INTO OrderItems (OrderID, ItemID, Quantity)\
            VALUES (?, ?, ?)", (OrderID, ItemID, Quantity,));
        current_quantity = conn.execute("SELECT Quantity FROM Inventory WHERE ItemID = ?", (ItemID,))
        new_quantity = current_quantity - Quantity
        conn.execute("UPDATE Inventory SET Quantity = ? WHERE ItemID = ?", (new_quantity,ItemID,))

    #Insert PurchaseHistory table info with calculated total
    conn.execute("INSERT INTO PurchaseHistory (OrderID, UserID, Total)\
            VALUES (?, ?, ?)", (OrderID, UserID, total,));




# MAIN FUNCTION CALL
if __name__ == "__main__":
    main()