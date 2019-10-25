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

    # login and validation (if it doesn't return a boolean, change this to accept a username.)
    userID = login.ValidateUser()
    session = homeScreen(userID)

    # TODO This function may can be called within the displayTable() Function
    #      to allow the display table to update itself and take load off the main
    #      function
    addToCart()

    


def homeScreen(userID):
    currentUser = userID
    conn = sqlite3.connect('store.db')
    exitStore = 0

    while (exitStore != 1):
        try:
            print("\nStore Options:\n1. View Inventory\n2. View Past Orders\n0. Exit Store\n")
            userSelection = int(input("Select an option: "))

            if (userSelection) == (1):
                displayTable(conn)
            elif (userSelection) == (2):
                print("past orders\n")
                displayOrderHistory(conn, currentUser)
            elif (userSelection) == (0):
                print("\n**********************************")
                print("*  Thanks for Shopping with us!  *")
                print("**********************************\n")
                exit()

        except Exception as ex:
            print("Please enter a store option.\n")

    return conn

def displayOrderHistory(conn, currentUser):
    userID = conn.execute('SELECT UserID FROM Users WHERE Username = currentUser')
    cursor = conn.execute('SELECT * FROM PurchaseHistory WHERE UserID = UserID')

    print('{:<10s}{:>25s}{:>30s}{:>35s}{:>45s}'.format("\nPurchase ID", "Order ID", "User ID",
                                                       "Total", "Credit Card"))
    for row in cursor:
        print('{:<10d}{:<25d}{:<30d}{:<35.2f}{:<45d}'.format(row[0], row[1], row[5],
              row[3], row[4]))


def displayTable(conn):

    # TODO Add this function that will display the items from the Database that will be available
    #      add to cart.

    cursor = conn.execute('SELECT * FROM Inventory GROUP BY Category')

    print('{:<10s}{:<25s}{:<30s}{:<35s}{:<45s}{:<50s}'.format("\nItem ID", "Name", "Quantity",
                                                              "Price","Category", "Desc"))

    for row in cursor:
        print('{:<10d}{:<25s}{:<30d}{:<35.2f}{:<45s}{:<50s}'.format(row[0], row[1], row[5],
              row[3], row[4], row[2]))
    print("\n")

    return



def addToCart(itemID, itemQuantity):

    # TODO This function will be responsible for adding an item to a shopping cart.
    cart = [[]]
    for each in cart:
        itemID.append(cart)
        for object in cart:
            itemQuantity.append(cart)
    return


def confirmPurchase(UserID, cart):

    #First insert into the orders table to create the orderID
    conn.execute ("INSERT INTO Orders (UserID)\
        VALUES (?)", (UserID));

    #Select the most recent orderID for the user
    OrderID = conn.execute("SELECT MAX(OrderID) FROM Orders WHERE UserID = ?", (UserID))

    #Insert the itemID's and their quantities into the OrderItems Table
    total = 0
    for item in cart:
        price = 0
        ItemID = [item][0]
        Quantity = [item][1]
        price = conn.execute ("SELECT Price FROM Inventory WHERE ItemID = ItemID")
        total += price * Quantity
        conn.execute ("INSERT INTO OrderItems (OrderID, ItemID, Quantity)\
            VALUES (?, ?, ?)", (OrderID, ItemID, Quantity));

    #Insert PurchaseHistory table info with calculated total
    conn.execute ("INSERT INTO PurchaseHistory (OrderID, UserID, Total)\
            VALUES (?, ?, ?)", (OrderID, UserID, total));


# MAIN FUNCTION CALL
if __name__ == "__main__":
    main()