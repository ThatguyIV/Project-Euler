def isPrime(number):
  '''
  returns True if a number is prime
  returns False if not.
  '''
  if number <= 1:
    return False
  elif number <= 3:
    return True
  elif number % 2 == 0 or number % 3 == 0:
    return False
  x = 5
  while x * x <= number:
    if number % x == 0 or number % (x + 2) == 0:
      return False
    x = x + 6
  return True
def findFactors(number):
  '''
  returns a list of all the factors of a number
  '''
  numlist = []
  for i in range(2, number):
    if number % i == 0:
      numlist.append(i)
  return numlist

testnum = 600851475143
primeFactors = []
for i in findFactors(testnum):
  if isPrime(i):
    primeFactors.append(i)
    print(primeFactors)
print(primeFactors)
