shirt_count=0
size_s=0
size_m=0
size_l=0
total_size=4

while True:
    shirt_type=input("enter shirt size you'd like to buy(s/m/l) or 'exit' to quit: ")
    
    if shirt_type.lower().startswith('e'):
        print()
        break
    elif shirt_type.lower()=="s":
        size_s+=1
    elif shirt_type.lower()=="m":
        size_m+=1
    elif shirt_type.lower()=="s":
        size_l+=1
    else:
        print("invalid entry counted as m")
        size_m+=1
    
    shirt_count+=1
    if shirt_count>=total_size:
        print("\nAll shirts are sold out")
        break
print(shirt_type,"Shirts total", size_s, "small size, ", size_m, " medium size, ",size_l," large size")