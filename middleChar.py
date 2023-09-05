def get_middle(s):
  
    m2= int(len(s)/2)
    if (m2%2==0):       #even so only 1
        print("Got here" +m2)
        s=s[m2-1]
    elif (m2%2!=0):
        s=s[m2-1:m2+1]
    return s


print(get_middle("st"))

