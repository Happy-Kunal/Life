import element
import random as _random

class Myelement(element.Element):

    def __int__(self):

        super().__init__()

    # new size of daughter blob 
    def daughter_size(self):

        change_in_size=_random.randrange(0,10)

        # if daughter blob is identical to parent
        if change_in_size==5:

            pass
        
        # if daughter blob is smaller than parent
        elif change_in_size<5:
            
            self.data['size']-=change_in_size
        
        # if daughter blob is larger than parent
        else:

            self.data['size']+=change_in_size

        return self.data['size']

    # new speed of daughter blob
    def daughter_speed(self):

        pass
    

if __name__ == "__main__" :
    
    # Creating very first instance 
    e0 = Myelement()
    print(f"e0 : {e0}")

    # Syntetically Giving Food
    e0.data["food"] = 10
    
    # Storing  Reproduced Object
    e1 = e0.daypassed()
    print(f"e1 : {e1}")
    
    # Alive members
    print()
    print(f"Alive Dict : {Myelement.Alive}")
    print()
    
    # Killing e1
    e1.died("Loneliness / Lack Of Friends")
    
    # Proof that e1 isn't yet killed by garbage collector
    print(f"e1 : {e1}")
    
    # Proof that e1 doesn't Exists in Alive Dict
    print()
    print(f"Alive Dict : {Myelement.Alive}")

    # reproduction

    print(e0.daughter_size())
