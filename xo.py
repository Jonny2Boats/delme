def xo(s):
    s=s.lower()
    xs=s.count("x")
    os=s.count("o")
    
    if xs==os :
        return True
    else:
        return False

print(xo("zzoo"))
