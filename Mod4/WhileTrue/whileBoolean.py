# review and run GREET COUNT
greet_count=5

# loop while count is greater than 0
while greet_count>0:
    print(greet_count,"!")
    greet_count-=1
print("\nIGNITION!")

animal_count=4
animal_name=""
num_animals=0
all_animals=[]

while animal_count>0:
    animal_name=input("key in an animal name: ")
    animal_count-=1
    num_animals+=1
    
    if animal_name.lower().startswith('exit'):
        print("Understood, exit")
        break
    else:
        pass
    
    all_animals.append(animal_name)
    
if all_animals.isalpha()==True:
    print(animal_name)
else:
    print("no animals")