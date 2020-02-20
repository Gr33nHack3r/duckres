#!/usr/bin/env python

#############################################################################################################
def prop(x_image,y_image,x_ratio,y_ratio):
    
    divimg = (x_image / y_image) # resolution image ratio
    divrat = (x_ratio / y_ratio) # screen ratio
    
    n = len(str(x_image)) - 2 # calculating the level of precision
    
    # decreasing the witdh resolution until the image ratio and the screen ratio are equal       
    if divimg <= divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):
            y_image -= 1
            
    # decreasing the height resolution until the image ratio and the screen ratio are equal
    elif divimg > divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):   
            x_image -= 1
                      
    # returning the results
    return x_image, y_image

#############################################################################################################
def printprop(x_image,y_image,x_ratio,y_ratio):
    x_result, y_result = prop(x_image,y_image,x_ratio,y_ratio) # setting the variables as result
    print("x = " + str(x_result)), print("y = " + str(y_result)) # printing the variables
    
#############################################################################################################
def autocrop(file,x_ratio,y_ratio):
    from PIL import Image
    with Image.open(file) as im:
        y_image, x_image = im.size # setting the (input image resolution)
        x_out, y_out = prop(x_image,y_image,x_ratio,y_ratio) # setting (output image resolution)
        
        # setting pixel to crop       
        y_cut = int((y_image - y_out) / 2)
        x_cut = int((x_image - x_out) / 2)
        
        # crop image when (output image resolution) and (input image resolution) are different
        if y_out != y_image:
            img_crop = im.crop(())
        
        elif x_out != x_image:
            img_crop = im.crop(())
            
        # saving the image
        img_crop.save(str(file)+'_cropped.png','PNG')