def correct(string):
  strArray = list(string)
  i = 0
  while (i < len(strArray)) :
    if strArray[i] == "0" :
      strArray[i] = "O"
    if strArray[i] == "5" :
      strArray[i] = "S"
    if strArray[i] == "1":
      strArray[i] = "I"
    i = i + 1
  print( "".join(strArray))
correct("DUBL1N")
