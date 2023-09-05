# return masked string
def maskify(cc):
    cOut=""
    lcc=len(cc)
    loopCount= 0
    
    if lcc <4: return cc

    for i in cc:
        if loopCount < (lcc-4):
            cOut+= "#" 
        elif loopCount < lcc:
            cOut+= str(i)
        loopCount += 1


    return cOut 

print(maskify("123"))