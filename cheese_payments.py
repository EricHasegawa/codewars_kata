import math
def pay_cheese(arr):
    totalMinutes = 0
    x = 0
    while (x < len(arr)) :
        totalMinutes = totalMinutes + ((arr[x] / 10 * 6))
        x = x + 1
    return "L" + str(int((math.ceil(totalMinutes / 60) * 8.75 * 4)))
