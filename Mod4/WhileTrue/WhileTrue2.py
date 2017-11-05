# [ ] review WHAT TO WEAR code then run testing different inputs

while True:
    weather=input("Enter weather (snowy, rainy, sunny or quit): ")
    print()
    
    if weather.lower()=="sunny":
        print("Wear a t-shirt and sunscreen")
        break
    elif weather.lower()=="rainy":
        print("Bring an umbrella and boots")
        break
    elif weather.lower()=="snowy":
        print("Wear a warm coat and hat")
        break
    elif weather.lower().startswith("q"):
        print("quit detected, exiting")
        break
    else:
        print("sorry not sure what to suggest for ",weather,"\n")
