# Review and run code
# this example never loops because the break has no conditions
while True:
    print('write forever, unless there is a "break"')
    break

# [ ] review the NUMBER GUESS code then run - Q. what cause the break statement to run?
secret_number="5"

while True:
    number_guess=input("guess the number 1-5: ")
    if number_guess==secret_number:
        print("Yes," , number_guess, "is correct!\n")
        break
    else:
        print(number_guess," is incorrect\n")

