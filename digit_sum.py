def digit_sum(n):
    temp=0
    ns=str(n)
    length= len(ns)
    for i in range(0,length):
        temp+=int(ns[i])
        #print(temp)
    return temp


print(digit_sum(1234))
