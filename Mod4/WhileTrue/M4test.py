def str_analysis():
    while True:
        message=input("enter word of integer: ")
        if message.isalpha()==True:
            print('"'+message+'"',"is all alphabetical characters!")
            break
        elif message.isdigit()==True:
            if int(message)>=99:
                print(str(message),"is a pretty big number")
                break
            else:
                print(str(message),"is a smaller number than expected")
                break
        elif message!="":
            print('"'+message+'"',"is neither alpha nor all digit")
            break
        else:
            message=input("enter word of integer: ")
    return
str_analysis()
