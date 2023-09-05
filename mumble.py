def accum(s):
    # 1st char 1 caps
    # therafter Caps & i (in loop) chars, sep with -
    
    
    outString=""
    counter= 1
    
    for i in range(0,len(s)):
        #outString+= s[i]
        if (i==0):
            outString+= s.upper()[i] +"-"
            counter +=1
        if (i>=1):
            #1st cap always printed
            outString+= s.upper()[i]
            #Then loop counter times
            for j in range(1,counter):
                outString+= s.lower()[i] 
            #Add dash
            outString+="-"
            counter+=1
#nasty cheat- got a "-" at the end of the above, so skim that off the end
    outString= outString[:-1]

    return outString

print(accum("RqaEzty"))