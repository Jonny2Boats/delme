def filter_list(l):
    'return a new list with the strings filtered out'
    newl=[]
    for i in l:
        print(type(i))
        if type(i) is int:
            newl.append(i)

    return newl

print(filter_list([1,2,'aasf','1','123',123]))