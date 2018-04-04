def high_and_low(numbers):
  x = list(map(int,numbers.split(" ")))
  return ( str(max(x)) + " " + str(min(x)))
  
high_and_low("1 2 3 4 5") 
