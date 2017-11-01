#Program: [ ] 3 Guesses
#use nested if statements complete the flowchart code
#create a bird_names string variable with the names of 1, 2, 3 or more birds to make it easier
#get bird_guess input and use bird_guess in bird_names to generate Boolean True/False
#if the the guess is wrong (False) create a sub test until the user has had 3 guesses

guess_b=input("Guess the bird: ")
b="hawk"

if guess_b.lower()!=b.lower():
    print(guess_b.lower()=b.lower(),"2nd try")
    b2=input("2nd guess: ")
    print()
    
    if b2.lower()!=b.lower():
        print(b2.lower()!=b.lower(),"3rd try")
        b3=input("3rd guess: ")
        print()
        
        if b3.lower()!=b.lower():
            print("Sorry out of tries")
        else:
            print("Yes, 3rd try!")
    
    else:
        print("Yes, 2nd try!")

else:
    print("Yes, 1st try!")
    
    