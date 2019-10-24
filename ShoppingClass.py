



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
			
			