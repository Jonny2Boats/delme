def likes(names):

    if len(names)==0: 
       
        return "No one likes this"
    
    elif len(names)==1: 
        #print(names)
        return str(names[0]) +" likes this"

    elif len(names)==2: 
        #print("2" + str(names))
        return str(names[0]) + " and "+ str(names[1]) + " like this"
    
    elif len(names)==3:
        return str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) +  " like this"

    else:
        return str(names[0]) + ", " + str(names[1]) + " and " + str(len(names)-2) + " others like this"




# pass in array of names
print((likes(["Peter"])))
print((likes(["Jacob", "Alex"])))
print((likes(["Max", "John", "Mark"])))
print((likes(["Alex", "Jacob", "Mark", "Max"])))


'''[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"'''