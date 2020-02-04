#!/usr/bin/env python

def prop(x_image,y_image,x_ratio,y_ratio):
    divimg = (x_image / y_image)
    divrat = (x_ratio / y_ratio)
    
    n = len(str(x_image)) - 2
           
    if divimg <= divrat:
        print("entrato1")
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):
            y_image -= 1
        print("x = " + str(x_image)), print("y = " + str(y_image))
        
    elif divimg > divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):   
            x_image -= 1
        print("x = " + str(x_image)), print("y = " + str(y_image))
