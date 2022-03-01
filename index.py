class NBA_player:
    def __init__(self, name, position, number, mvp, points):
        self.name = name
        self.position = position
        self.number = number
        self.mvp = mvp
        self.points = points 

    def Basketball_card(self):
        print("His Name is " + self.name + " his position is the" ,self.position)

    def Basketball_Awards(self):
        print(self.name + " has this many MVPs:", self.mvp,)  

    def Basketball_jersey(self):
        print(self.name + "'s" + " Jersey number is:", self.number)
    
    def New_mvp_award(self):
        print("Congrats to " + self.name +" For MVP award number" , self.mvp + 1) 
    
    def Shoot_basket(self,jumpshot):
        self.points += jumpshot 

         
        



MJ = NBA_player("Micheal Jordan", "Shooting Guard", 23, 6, 50)
Magic = NBA_player("Magic Johnson", "Point Guard", 32, 5, 20)
Bird = NBA_player("Larry Bird", "Small Forward", 33, 3, 26)
print("Player Name: " + MJ.name)
print(MJ.position)
MJ.Basketball_card()
MJ.Basketball_Awards()
MJ.Basketball_jersey()
MJ.New_mvp_award()
MJ.Shoot_basket(20)
print(MJ.points)
print(" ")

print("Player Name: " + Magic.name)
print("Player Position: "+ Magic.position)
Magic.Basketball_card()
Magic.Basketball_Awards()
Magic.Basketball_jersey()
Magic.New_mvp_award()
Magic.Shoot_basket(10)
print(Magic.points)
print(" ")

print("player Name: " + Bird.name)
print("Player Position: " + Bird.position)
Bird.Basketball_card()
Bird.Basketball_Awards()
Bird.Basketball_jersey()
Bird.New_mvp_award()
Bird.Shoot_basket(20)
print(Bird.points)
print(" ")


