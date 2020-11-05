import math as _math

# Element Class For Creating Liveable Creatures In Simulation
class Element :
    
    Idnum = 0
    Alive = {}
    
    def __init__(self , location = (0 , 0) , life = _math.inf , **data) :
        
        self.location = location
        self.life = life
        self.data = data
        self.id = self.Idnum
        self.data["initial_life"] = life
        self.data["food"] = 0
        
        Element.Idnum += 1
        Element.Alive[self.id] = self
        
    def daypassed(self) :
        
        if (self.data["food"] >= 2):
            
            return self.reproduce(self.location , self.life , **self.data)
        
        elif (self.data["food"] == 1) :
            
            self.data["food"] -= 1
            
        else :
            
            self.died("starvation")
        
        # Life expectance
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
      
      
