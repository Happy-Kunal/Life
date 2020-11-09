# python program to create food instance
import random as _random
import math as _math

class food():

    def __init__(self,location=(0,0)):

        # randomly finding an angle so that we can get the polar coordinates
        # for food (as same as defined by kunal for movement of blob)
        rotate_angle = _random.randrange(0, 360 , 10)

        # polar coordinates
        movex = 1 * _math.cos(_math.radians(rotate_angle))
        movey = 1 * _math.sin(_math.radians(rotate_angle))

        self.location = (location[0] + movex , location[1] + movey)

# function which creates list of food instances for manipulation
def food_locations(quantity_of_food):

    f_list=[]

    for i in range(quantity_of_food):

        f_i=food()

        f_list.append(f_i)

    return f_list

if __name__=='__main__':

    print(food_locations(50))
    x=food_locations(34)

    


