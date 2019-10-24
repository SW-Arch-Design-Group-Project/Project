def main():
    print("\n***************************")
    print("*  Welcome to the Store!  *")
    print("***************************\n")


    #login and validation (if it doesn't return a boolean, change this to accept a username.)
    valid = login()
    while valid == False:
        print("Invalid login: Please try again!\n")
        login()


    displayTable()

    # TODO This function may can be called within the displayTable() Function
    #      to allow the display table to update itself and take load off the main
    #      function
    addToCart()

    print("\n**********************************")
    print("*  Thanks for Shopping with us!  *")
    print("**********************************\n")
    return





def login():

    # TODO Change to real login function

    print("Login:")
    Username = input("Enter a username: ")
    passWord = input("Enter a password: ")
    print()

    if Username == "Username":
        if passWord == "Password":
            return True
    
    else:
        return False






def displayTable():

    # TODO Add this function that will display the items from the Databse that will be available
    #      add to cart.

    print("Table of items will go here.")
    return





def addToCart():

    # TODO This function will be responsible for adding an item to a shopping cart.

    return



# MAIN FUNCTION CALL
if __name__ == "__main__":
    main()