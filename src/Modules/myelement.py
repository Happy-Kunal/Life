import element
import random as _random
import math as _math
import food

class Myelement(element.Element):

    def __int__(self):

        super().__init__()

    # new size of daughter blob 
    def daughter_size(self):

        change_in_size_1=_random.choice(['Increase','Decrease','Identical'])
        change_in_size_2=_random.randrange(0,10)

        # if daughter blob is larger than parent
        if change_in_size_1=='Increase':

            self.data['size']+=change_in_size_2
        
        # if daughter blob is smaller than parent
        elif change_in_size_1=='decrease':
            
            self.data['size']-=change_in_size_2
        
        # if daughter blob is identical to parent
        else:

            pass

        return self.data['size']

    # new speed of daughter blob
    def daughter_speed(self):

        change_in_speed_1=_random.choice(['Increase','Decrease','Identical'])
        change_in_speed_2=_random.randrange(0,10)

        # if daughter blob is larger than parent
        if change_in_speed_1=='Increase':

            self.data['size']+=change_in_speed_2
        
        # if daughter blob is smaller than parent
        elif change_in_speed_2=='Decrease':
            
            self.data['size']-=change_in_speed_2
        
        # if daughter blob is identical to parent
        else:

            pass

        return self.data['size']

    # new sensing capability of blob
    def sensing_capability(self):

        pass

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

    # grab food if blob find it in its path    
    def grab_food(self) :

        print(self.location)
        f_list=food.food_locations(1000)

        if self.data['size']:
            pass

        food_eaten=0
        for i in f_list:

            # self.move() # if sense of blob is assumed completely zero 

            if self.location == i.location:
                
                # print(i.location)
            
                del i
                
                # print('food found')

                food_eaten+=1

            else:

                pass

        self.data['food']=food_eaten

        return self.data['food']

        

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
    
    # Proof t~hat e1 isn't yet killed by garbage collector
    print(f"e1 : {e1}")
    
    # Proof that e1 doesn't Exists in Alive Dict
    print()
    print(f"Alive Dict : {Myelement.Alive}")

    # reproduction

    print(e0.daughter_size())
    print(e0.daughter_speed())

    # # food grabing
    # print(e0.move())
    # while True:
    #     a=e0.grab_food()
    #     print(a)


    # food grabing
    print(e0.move())
    a=e0.grab_food()
    print(a)