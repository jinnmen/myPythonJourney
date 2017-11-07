long_num=""
int_num="0"

while int_num.isdigit() == True:
    int_num = input("enter digit\'s only (Digits only, No spaces): ")
    long_num+=int_num
print("\n" + long_num,"is the total")
