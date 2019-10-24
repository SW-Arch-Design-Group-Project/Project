



class item : 

    # initializer
    # called by python at object creation time
    def __init__( self, aName = "THINGIE", aPrice = 0 ) :

        self.name = aName
        self._price = aPrice   # private data, don't access directly
                               # use set_price and get_price

    # string conversion method
    # called by python when printing a thingie object
    def __str__( self ) :

        # $xx.xx name
        s = "$" + format( self._price, "5.2f" ) + " " + self.name
        return s


    # price accessor method
    # returns the price
    def get_price( self ) :

        return self._price
    
    def get_name(self):
       
        return self._aName


    # price mutator method
    # changes the price
    #   if new price is < 0, does NOT change price
    def set_price( self, newPrice ) :

        if type( newPrice ) is not int and type( newPrice ) is not float :
            print( "ERROR: thingie price must be a number, not", newPrice )
            return

        # make sure price is non-negative
        if newPrice < 0 :
            print( "ERROR: thingie price must be non-negative" )
        else :
            self._price = newPrice
			

class Cart:
    
    def __init__(self, list):
        self.list = []
    
    #add items to the list
    def addItem(self, item);
        self.list.append(self.list)
    
    #get the total of all items in cart
    def getTotal(self): 
        total = 0;
        for item in self.list:
            name, price = item
            total = total + price
    #get number of items in the cart
    def getNumItems(self):
        count = 0
        for c in range(self.list):
            count = self.list + 1
            return count
    
    #remove items from the cart
    def removeItem(self, item)
    
    
    
        
        
        
			