white_L=1
white_M=1
blue_M=1
blue_S=1
available=False

def shirts():
    keyin=input("Key in color and size for order: ")
    if "white".lower() and "l".lower() in keyin:
        print("Available, confirm to order", keyin)
        available=True
    elif "white".lower() and "m".lower() in keyin:
        print("Available, confirm to order", keyin)
        available=True
    elif "blue".lower() and "l".lower() in keyin:
        print("Available, confirm to order", keyin)
        available=True
    elif "blue".lower() and "m".lower() in keyin:
        print("Available, confirm to order", keyin)
        available=True
    else:
        print("Unavailable!")
    return

shirts()

    