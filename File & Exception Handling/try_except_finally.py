x = 10
try:
    if x < 18:
        raise Exception
    else:
        print("Access Granted!")

except:
    print("Access Denied", Exception)

finally:
    print("Program Ended!")
