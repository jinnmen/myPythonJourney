hello=input("Would you like to say hi(y/n)? ")


if hello.lower()=="y":
    #say full hello?
    full_h=input("Full Hello?(y/n): ")
    
    if full_h.lower()=="y":
        print("Hello!")
    else:
        print("Hi")
    elif hello.lower()=="n":
        print("friendly nod")

elif hello.lower()=="n":
    print("friendly nod")
    
else:
    print("I don't understand, please start again.")

hello2=input("Would you like to say hi(y/n)? ")
    