import sqlite3

conn = sqlite3.connect('store.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE User
         (UserID INTEGER PRIMARY KEY	 AUTOINCREMENT,
         Address         CHAR(100)   NOT NULL,
         Password        CHAR(50)    NOT NULL,
         Username        CHAR(50));''')

conn.execute('''CREATE TABLE Inventory
         (ItemID INTEGER PRIMARY KEY	AUTOINCREMENT,
         Name           CHAR(50)    NOT NULL,
         Description    CHAR(200)   NOT NULL,
         Price			REAL		NOT NULL,
         Category		CHAR(50)	NOT NULL,
         Quantity		INTEGER 	NOT NULL);''')

conn.execute('''CREATE TABLE Orders
        (OrderID INTEGER   PRIMARY KEY	AUTOINCREMENT,
        UserID   INTEGER   NOT NULL,
    	FOREIGN KEY (UserID) REFERENCES User(UserID));''')

conn.execute('''CREATE TABLE OrderItems
        (OrderID 	INTEGER		NOT NULL,
        ItemID		INTEGER		NOT NULL,
        Quantity    INTEGER		NOT NULL,
        PRIMARY KEY (OrderID, ItemID),
    	FOREIGN KEY (OrderID)	REFERENCES Orders(OrderID),
    	FOREIGN KEY (ItemID)	REFERENCES Inventory(ItemID));''')

conn.execute('''CREATE TABLE PurchaseHistory
        (PurchaseID INTEGER		PRIMARY KEY	AUTOINCREMENT,
        OrderID   	INTEGER		NOT NULL,
        UserID    	INTEGER		NOT NULL,
        Total		REAL		NOT NULL,
        CreditCard	INTEGER		NOT NULL,
    	FOREIGN KEY (OrderID)	REFERENCES Orders(OrderID),
    	FOREIGN KEY (UserID)	REFERENCES User(UserID));''')


conn.close()