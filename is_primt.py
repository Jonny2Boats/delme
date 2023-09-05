def is_prime(x):
  if (x <= 0) or (x==1) : return False
  for i in range(2,x-1):
    print( x% i)
    if (x % i) ==0:
      return False

  return True

print(is_prime(-1))