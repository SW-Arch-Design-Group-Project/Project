import sqlite3

def buildDatabase():
    conn = sqlite3.connect('store.db')


    print("Opened database successfully")

    conn.execute('''DROP TABLE IF EXISTS User''')
    conn.execute('''DROP TABLE IF EXISTS Inventory''')
    conn.execute('''DROP TABLE IF EXISTS OrderItems''')

    conn.execute('''CREATE TABLE IF NOT EXISTS User
            (UserID INTEGER PRIMARY KEY	 AUTOINCREMENT,
            Address         CHAR(100)   NOT NULL,
            Password        CHAR(50)    NOT NULL,
            Username        CHAR(50));''')

    conn.execute('''CREATE TABLE IF NOT EXISTS Inventory
            (ItemID INTEGER PRIMARY KEY	UNIQUE,
            Name           CHAR(50)    NOT NULL UNIQUE,
            Description    CHAR(200)   NOT NULL,
            Price			REAL		NOT NULL,
            Category		CHAR(50)	NOT NULL,
            Quantity		INTEGER 	NOT NULL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS Orders
            (OrderID INTEGER   PRIMARY KEY	AUTOINCREMENT,
            UserID   INTEGER   NOT NULL,
            FOREIGN KEY (UserID) REFERENCES User(UserID));''')

    conn.execute('''CREATE TABLE IF NOT EXISTS OrderItems
            (OrderID 	INTEGER		NOT NULL,
            ItemID		INTEGER		NOT NULL,
            Quantity    INTEGER		NOT NULL,
            PRIMARY KEY (OrderID, ItemID),
            FOREIGN KEY (OrderID)	REFERENCES Orders(OrderID),
            FOREIGN KEY (ItemID)	REFERENCES Inventory(ItemID));''')

    conn.execute('''CREATE TABLE IF NOT EXISTS PurchaseHistory
            (PurchaseID INTEGER		PRIMARY KEY	AUTOINCREMENT,
            OrderID   	INTEGER		NOT NULL,
            UserID    	INTEGER		NOT NULL,
            Total		REAL		NOT NULL,
            CreditCard	INTEGER		NOT NULL,
            FOREIGN KEY (OrderID)	REFERENCES Orders(OrderID),
            FOREIGN KEY (UserID)	REFERENCES User(UserID));''')

    
    conn.execute ("INSERT INTO User (Address, Password, Username)\
        VALUES ('75 B. S. Hood Road, Mississippi State, MS 39762', 'SWARCH2019', 'User')");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('Pledge', 'Lemon scented Pledge', 8.00, 'Household items', 20)");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('Bleach', 'Used for bathroom cleaning', 5.00, 'Household items', 15)");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('Toy Train', 'Wooden Toy Train', 10.00, 'Toys', 30)");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('Lego Set', 'Lego Star Wars set', 150.00, 'Toys', 10)");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('The Institute', 'Hardcover Book', 30.00, 'Books', 4)");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('Radio', 'Small portable radio', 25.00, 'Small electronics', 5)");

    conn.execute ("INSERT INTO Inventory (Name, Description, Price, Category, Quantity)\
        VALUES ('Walkie-Talkie' , 'Pair of portable communication devices', 40.00, 'Small electronics', 10)");

    conn.commit()

    conn.close()


    #cursor = conn.execute("SELECT ItemId, Name, Description, Price, Category, Quantity from Inventory")

    #for row in cursor:
    #   print ("ItemID = ", row[0])
    #   print ("NAME = ", row[1])
    #   print ("Description = ", row[2])
    #   print ("Price = ", row[3])
    #   print ("Category =", row[4])
    #   print ("Quantity =",row[5])

    return