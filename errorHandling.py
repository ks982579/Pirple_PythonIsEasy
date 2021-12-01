
try:
    #myNum = float("N/A")
    raise TypeError("Only Floats Allowed")
except ValueError as e:
    print(str(e))
except Exception as ee:
    print("not sure what went wrong")
    print("Error Message: {}".format(ee))
finally:
    print("I always run")
print("I didn't quit")