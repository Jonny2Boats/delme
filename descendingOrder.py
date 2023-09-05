def descending_order(num):

    return num


smallNo= 123456789
thisNo= []

smallNo=str(smallNo)
for i in range(0,len(smallNo)):
    thisNo.append(smallNo[i])
thisNo.sort(reverse=True)
print(thisNo)
thisNo= int("".join(thisNo))
print(thisNo)
