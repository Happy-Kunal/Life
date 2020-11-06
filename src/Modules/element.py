import math as _math
import random as _random

# Element Class For Creating Liveable Creatures/Blob In Simulation
class Element :
    
    Idnum = 0
    Alive = {}
    
    def __init__(self , location = (0 , 0) , life = _math.inf , **data):
        self.location = location
        self.life = life
        self.data = data
        self.id = self.Idnum
        self.data["initial_life"] = life
        self.data["food"] = 0
        self.step = 1
        self.food_grabing_radius = 1

        Element.Idnum += 1
        Element.Alive[self.id] = self
    # this function gonna be triggred to pass a day in the simulation
    def daypassed(self) :
        # since food is the most important if an element/Blob got one Food
        # it will gonna  survive for next day if got two food gonna
        # survive for next day and Reproduce itself 
        if (self.data["food"] >= 2):
            
            return self.reproduce(self.location , self.life , **self.data)
        
        elif (self.data["food"] == 1) :
            
            self.data["food"] -= 1
            
        else :
            
            self.died("starvation")
        
        # Life expectance : sometimes user may wants to give a limited
        # life to its elements(Creatures / Blob) in that case it is important to
        # check weather its time for death of Element/Blob or not
        if self.life > 0 :
            
            self.life -= 1
            
        else :
            
            self.died("getting too old")
            
    def died(self , msg) :
            
            print(f"Element {self.id} died due to {msg}")
            del Element.Alive[self.id]
            
    @classmethod
    def reproduce(Element , location , life  , **data) :
          
          return Element(location , life , **data)

    # this function decides were blob (Element) wants to move and updates
    # its location 
    def move(self) :
        # randomly finding an angle so that we can get the polar coordinates
        # for blob to move
        rotate_angle = _random.randrange(0, 360 , 10)

        # polar coordinates
        movex = self.step * _math.cos(_math.radians(rotate_angle))
        movey = self.step * _math.sin(_math.radians(rotate_angle))

        self.location = (self.location[0] + movex , self.location[1] + movey)

    # blob can grab the food directly if the food is present within
    # the grabing range of Blob
    def grab_food(self) :

        pass

    




if __name__ == "__main__" :

# Creating very first instance 
    e0 = Element()
    print(f"e0 : {e0}")

# Syntetically Giving Food
    e0.data["food"] = 10

# Storing  Reproduced Object
    e1 = e0.daypassed()
    print(f"e1 : {e1}")

# Alive members
    print()
    print(f"Alive Dict : {Element.Alive}")
    print()

# Killing e1
    e1.died("Loneliness / Lack Of Friends")

# Proof that e1 isn't yet killed by garbage collector
    print(f"e1 : {e1}")

# Proof that e1 doesn't Exists in Alive Dict
    print()
    print(f"Alive Dict : {Element.Alive}")


