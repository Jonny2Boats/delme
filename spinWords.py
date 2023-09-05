def spin_words(sentence):
    # Your code goes here
    # if >4 then reverse
    s= sentence.split() 
    sOut=""
    for i in s:
        if len(i)>= 4:
            #backW = ''.join(reversed(i))
            backW= i[::-1]
            sOut= sOut + backW +" "
        else:
            sOut = sOut+ i + " "
    return sOut.strip()

print(spin_words("how now broown coow"))