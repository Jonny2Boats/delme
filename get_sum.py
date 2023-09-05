def get_sum(a,b):
    # a+ .... b
   # print( range(a,b))
   return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))


print(get_sum(1,2))
