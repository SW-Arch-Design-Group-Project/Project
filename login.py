
def ValidateUser():
    print("\n---------------- User Login ----------------\n")
    userLogin = str()       # User input for username credential
    userPasswd = str()      # User input for password credential
    validate = False

    # Loop until user enters correct credentials
    while (validate == False):
        try:
            print("Enter 'exit' as a Username to close the store.\n")
            userLogin = str(input("Username: "))        # Get username input
            
            if userLogin == "exit":
                exit()
            
            userPasswd = str(input("Password: "))       # Get password input
            userDatabase = "user credentials.txt"       # Get user credentials file

            # Open credentials file and parse entries
            with open(userDatabase, 'r') as credentialsFile:
                next(credentialsFile)
                eof = False

                while (eof == False):
                    line = credentialsFile.readline().strip("\n").split(",")        # Read-in one, split by commas, and append to list

                    # Check if user input matches credentials in file
                    if ((userLogin) == (line[1])) and ((userPasswd) == (line[2])):
                        """
                        Assign validate to true and break from loop. This section can be changed later
                        to return if valid or call other functions. (Depending on how we structure the
                        rest of the program).
                        """
                        print("\n")
                        eof = True
                        validate = True
                        return userLogin

                    elif (line[0] == ''):
                        raise Exception("\nInvalid Credentials! Please Try again.\n")

        except Exception as ex:
            print("\nInvalid Credentials! Please Try again.\n")

if __name__ == '__main__':
    ValidateUser()