def fizz_buzz(value):
  retVal = None # always initialize variable with None to avoid unboundError
  if value % 3 == 0 and value % 5 == 0:
      retVal = 'fizzBuz'
  elif value % 3 == 0:
     retVal = 'fizz'
  elif value % 5 == 0:
    retVal = 'buzz'
  else: 
     retVal = value
  return retVal


result = fizz_buzz(7)
print(result)