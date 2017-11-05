familiar_name=""

while True:
    familiar_name=input("Key in a common name friends/family use: ")
    print()
    
    if familiar_name.isalpha()==True:
        print("Greetings, ",familiar_name, "\n")
        break
    else:
        print("Try again without space and use alphabets")
        