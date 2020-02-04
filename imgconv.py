def prop(aspx,aspy,resx,resy,risx,risy):
    
    if (aspx / aspy) == (resx / resy):
        
        if aspx <= risx or aspx > and aspy == risy:
            while ("%.3f"%(resx / resy)) != ("%.3f"%(risx / risy)):
                resy -= 1
            return print("x = "+str(resx)), print("y = "+str(resy))
        
        elif aspx == risx and aspy < risy:
            while ("%.3f"%(resx / resy)) != ("%.3f"%(risx / risy)):
                resx -= 1
            return print("x = "+str(resx)), print("y = "+str(resy))
    
    else:
        raise Exception("resolution != aspect")