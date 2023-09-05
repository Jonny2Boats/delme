def is_isogram(string):
    #your code here
    isISO= True
    string= string.lower()
    for i in list(map(chr, range(97, 123))):
        tempCount= string.count(i)
        if tempCount>1: isISO=False
        print(" " + str(i) + str(tempCount))
    return isISO

print(is_isogram("moOse"))
