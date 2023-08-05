try:
    x = 5
    x / 1
    x + 3
    x = {}
    x
except ZeroDivisionError:
    print("can not divide by zero")
except TypeError:
    print("Can not sort out the the operands")
else:
    print("An unknown error occured")
finally:
    print("Closing up all network resources")