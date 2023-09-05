def high_and_low(numbers):
    tempNo= 0.0
    numbers= numbers.split()
    print(numbers)
    for i in numbers:
       print(i)
       tempNo+= int(i)
    return numbers


print(high_and_low("1,2,3"))

