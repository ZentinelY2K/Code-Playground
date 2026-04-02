class Laptop:

    def __init__(self,make,processor,year,color): #short for initialize
        """
        'self' refers to the class you're working on, hence the obvious chocie of words 'self'

        The variables below are the attributes of the Laptop class, which are passed by the user as arguments
        """
        self.make = make
        self.processor = processor
        self.year = year
        self.color = color

    def boot(self):
        print(f"{self.processor} Booting Up")
    
    def shutdown(self):
        print(f"{self.processor} Shutting Down")


        
Laptop = Laptop(1,"Intel i5",2,3)
Laptop.shutdown()