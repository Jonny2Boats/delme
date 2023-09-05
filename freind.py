def friend(x):
    #Code x = list of strings
    # Watch= remove i from x resets the loop!!!
    out=[]

    for i in x:
        if len(i) == 4:         
            out.append(i)
    return out

print(friend(['Ryan','123','Cool Man']))
    