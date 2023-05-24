# error handling
def hoooohoooo():
    try:
        print("hoooohoooo")
    except:
        print("hoooohoooo")
    else:
        print("hoooohoooo")
    finally:
        print("hoooohoooo")


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor
