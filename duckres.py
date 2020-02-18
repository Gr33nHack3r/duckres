#!/usr/bin/env python

#############################################################################################################
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

#############################################################################################################
        
def autocut(file,x_ratio,y_ratio):
    from PIL import Image
    with open(file) as image:
    y_image, x_image = image.size # image resolution
    y_res, x_res = y_image, x_image # setting variables for the result
    
    divimg = (x_image / y_image) # resolution ratio
    divrat = (x_ratio / y_ratio) # screen ratio
    
    n = len(str(x_image)) - 2 # calculating the level of precision
    
    # decreasing the witdh resolution untile the image ratio and the screen ratio are equal
    if divimg <= divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):
            y_res -= 1
    
    # decreasing the height resolution until the image ratio and the screen ratio are equal
    elif divimg > divrat:
        while round((x_image / y_image), n) != round((x_ratio / y_ratio), n):
            x_res -= 1
    
    # setting the variables containing the pixel to crop       
    y_cut = int((y_image - y_res) / 2)
    x_cut = int((x_image - x_res) / 2)
    
    # cropping image if the screen ratio is major than the image ratio
    if divimg <= divrat:
        img_crop = image.crop((0,y_cut,0,y_cut))
    
    # cropping image if the screen ratio is minor than the image ratio
    elif divimg > divrat:
        img_crop = image.crop((x_cut,0,x_cut,0))
        
    # saving the image
    image.save('cropped', format= 'png')