shirt_count=0
size_s=0
size_m=0
size_l=0
total_size=4

cost_s=6
cost_m=7
cost_l=8

while True:
    shirt_type=input("enter shirt size you'd like to buy(s/m/l) or 'exit' to quit: ")
    
    if shirt_type.lower().startswith('e'):
        print()
        break
    elif shirt_type.lower()=="s":
        size_s+=1
    elif shirt_type.lower()=="m":
        size_m+=1
    elif shirt_type.lower()=="l":
        size_l+=1
    else:
        print("invalid entry counted as m")
        size_m+=1
    
    shirt_count+=1
    if shirt_count>=total_size:
        print("\nAll shirts are sold out")
        break
    
total_cost=(size_s*cost_s)+(size_m*cost_m)+(size_l*cost_l)    
print(shirt_count,"Shirts total", size_s, "small size, ", size_m, " medium size, ",size_l," large size")
print("$",total_cost,"Shirts total cost. $",size_s*cost_s, "small size cost, $",size_m*cost_m, "medium size cost, $",size_l*cost_l,"large size cost")