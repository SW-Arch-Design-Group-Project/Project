import login
import sqlite3

def main():
    print("\n***************************")
    print("*  Welcome to the Store!  *")
    print("***************************\n")


    #login and validation (if it doesn't return a boolean, change this to accept a username.)

    login.ValidateUser()

    displayTable()

    # TODO This function may can be called within the displayTable() Function
    #      to allow the display table to update itself and take load off the main
    #      function
    addToCart()

    print("\n**********************************")
    print("*  Thanks for Shopping with us!  *")
    print("**********************************\n")
    return




def displayTable():

    # TODO Add this function that will display the items from the Database that will be available
    #      add to cart.

    conn = sqlite3.connect('store.db')
    cursor = conn.execute('SELECT * FROM Inventory GROUP BY Category')

    print('{:<10s}{:<25s}{:<30s}{:<35s}{:<45s}{:<50s}'.format("Item ID", "Name", "Quantity", "Category", "Price", "Desc"))
    for row in cursor:
        print('{:<10d}{:<25s}{:<30d}{:<35f}{:<45s}{:<50s}'.format(row[0], row[1], row[5],
              row[3], row[4], row[2]))

    return





def addToCart():

    # TODO This function will be responsible for adding an item to a shopping cart.

    return



# MAIN FUNCTION CALL
if __name__ == "__main__":
    main()