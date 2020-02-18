#!/usr/bin/env python

def prop(x_image,y_image,x_ratio,y_ratio):
    divimg = (x_image / y_image) # resolution ratio
    divrat = (x_ratio / y_ratio) # screen ratio
    
    n = len(str(x_image)) - 2 #calculating the level of precision
    
    # decreasing the witdh resolution until the image ratio and the screen ratio are equal       
    if divimg <= divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):
            y_image -= 1
        print("x = " + str(x_image)), print("y = " + str(y_image))
    
    # decreasing the height resolution until the image ratio and the screen ratio are equal
    elif divimg > divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):   
            x_image -= 1
        print("x = " + str(x_image)), print("y = " + str(y_image))
