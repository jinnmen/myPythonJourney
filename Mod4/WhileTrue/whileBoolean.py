# review and run GREET COUNT
greet_count=5

# loop while count is greater than 0
while greet_count>0:
    print(greet_count,"!")
    greet_count-=1
print("\nIGNITION!")

animal_count=4
num_animals=0

while animal_count>0:
    animal_name=input("key in an animal name: ")
    animal_count-=1
    num_animals+=1
    all_animals=animal_name
    
    if animal_name.lower().startswith('exit'):
        print("Understood, exit")
        break
    else:
        pass
    
if all_animals.isalpha()==True:
    print(all_animals)
else:
    print("no animals")