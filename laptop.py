#Laptop program 
class laptop() :
    brand_name = "dell"
    generation = "11th"
    processor = "i3"
    def browsing(self) :
        print("iam using a laptop ", self.brand_name)
    def game(self):
        print("playing game")
        self.browsing()
    def files(self) :
        print("iam searching files in ... ",self.brand_name)
        self.game()
obj = laptop() 
obj.browsing()
obj.game()
obj.files()



