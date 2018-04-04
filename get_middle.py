def get_middle(s):
    x = list(s)
    mid = int(len(x))
    if (len(s) % 2 == 0):
      return(''.join(x[mid / 2 - 1 : mid / 2 + 1]))
    else :
      return(''.join(x[mid / 2 : mid / 2 + 1]))
