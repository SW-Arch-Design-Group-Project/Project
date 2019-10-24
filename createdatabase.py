import sqlite3

conn = sqlite3.connect('store.db')

print "Opened database successfully";

conn.execute('''CREATE TABLE User
         (UserID INT PRIMARY KEY     NOT NULL,
         Address         CHAR(100)   NOT NULL,
         Password        CHAR(50)    NOT NULL,
         Username        CHAR(50));''')

conn.execute('''CREATE TABLE Inventory
         (ItemID INT PRIMARY KEY    NOT NULL,
         Name           CHAR(50)    NOT NULL,
         Description    CHAR(200)   NOT NULL,
         Price			REAL		NOT NULL,
         Category		CHAR(50)	NOT NULL,
         Quantity		INT 		NOT NULL);''')

conn.execute('''CREATE TABLE Orders
        (OrderID INT   PRIMARY KEY    NOT NULL,
        UserID   INT   NOT NULL,
    	FOREIGN KEY (UserID) REFERENCES User(UserID));''')

conn.execute('''CREATE TABLE OrderItems
        (OrderID INT   NOT NULL,
        ItemID   INT   NOT NULL,
        Quantity    INT   NOT NULL,
        PRIMARY KEY (OrderID, ItemID),
    	FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    	FOREIGN KEY (ItemID) REFERENCES Inventory(ItemID));''')

conn.execute('''CREATE TABLE PurchaseHistory
        (PurchaseID INT    PRIMARY KEY   NOT NULL,
        OrderID   INT   NOT NULL,
        UserID    INT   NOT NULL,
        Total	REAL	NOT NULL,
        CreditCard	INT    NOT NULL,
    	FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    	FOREIGN KEY (UserID) REFERENCES User(UserID));''')


conn.close()