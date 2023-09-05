def factorial(n):
    n2=str(n)
    nOut=1
    for i in range(1,n+1):
        print("Im here : " + n2)
        nOut*= i
        print(nOut)
    return n

print("Out of loop" + str(factorial(4)))

  