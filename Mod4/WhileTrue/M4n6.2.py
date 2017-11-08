
def str_analysis():
    string=input("Key in something: ")
    if string.isdigit()==True:
        stringi=int(string)
        if stringi>99:
            print("big number!")
        else:
            print("small number")
    elif string.isalpha()==True:
        print("all about alpha")
    else:
        print("neither alpha nor digit")
    return

str_analysis()