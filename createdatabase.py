import sqlite3

def buildDatabase():
    conn = sqlite3.connect('store.db')


    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS User
            (UserID INTEGER PRIMARY KEY	 AUTOINCREMENT,
            Address         CHAR(100)   NOT NULL,
            Password        CHAR(50)    NOT NULL,
            Username        CHAR(50));''')

    conn.execute('''CREATE TABLE IF NOT EXISTS Inventory
            (ItemID INTEGER PRIMARY KEY	AUTOINCREMENT,
            Name           CHAR(50)    NOT NULL UNIQUE,
            Description    CHAR(200)   NOT NULL UNIQUE,
            Price			REAL		NOT NULL UNIQUE,
            Category		CHAR(50)	NOT NULL UNIQUE,
            Quantity		INTEGER 	NOT NULL UNIQUE);''')

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

    conn.execute ("INSERT INTO Inventory (Name,Description,Price,Category,Quantity)\
        VALUES ('pledge', 'lemon pledge', 5.00, 'Household items',20 )");

    conn.execute ("INSERT INTO Inventory (Name,Description,Price,Category,Quantity)\
        VALUES ('thomas the tank engine', 'toy wooden train', 10.00, 'Toys',10 )");

    conn.execute ("INSERT INTO Inventory (Name,Description,Price,Category,Quantity)\
        VALUES ('SWarch book', 'for some reason this book uses views and viewpoints', 69.00, 'Books',4 )");

    conn.execute ("INSERT INTO Inventory (Name,Description,Price,Category,Quantity)\
        VALUES ('Iphone 4', 'a literal dinosaur', 200.00, 'Small electronics',1 )");

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