def is_triangular(t):
    import math 
    x = (math.sqrt(8 * t + 1) - 1) / 2
    if x - int(x) > 0:
        return False
    else:
        return True
