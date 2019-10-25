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
    login.ValidateUser()

    session = homeScreen()

    # TODO This function may can be called within the displayTable() Function
    #      to allow the display table to update itself and take load off the main
    #      function
    addToCart()

    


def homeScreen():
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
            elif (userSelection) == (0):
                print("\n**********************************")
                print("*  Thanks for Shopping with us!  *")
                print("**********************************\n")
                exit()

        except Exception as ex:
            print("Please enter a store option.\n")

    return conn

def displayTable(conn):

    # TODO Add this function that will display the items from the Database that will be available
    #      add to cart.

    # conn = sqlite3.connect('store.db')
    cursor = conn.execute('SELECT * FROM Inventory GROUP BY Category')

    print('{:<10s}{:<25s}{:<30s}{:<35s}{:<45s}{:<50s}'.format("\nItem ID", "Name", "Quantity", "Price", "Category", "Desc"))
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



# MAIN FUNCTION CALL
if __name__ == "__main__":
    main()