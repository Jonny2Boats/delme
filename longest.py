def longest(a1, a2):
    # brogglin with sets
    out1=set(a1)
    out2=set(a2)
    out1=out1.update(out2)
    out1=sorted(out1)
    out1="".join(out1)
    
    return out1

print(longest("xyaabbbccccdefww","xxxxyyyyabklmopq"))