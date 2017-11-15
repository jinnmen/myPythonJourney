#Final correct version for test
def adding_report():
    intqlog=[] #one array for case "a"
    inttlog=[] #one array for case "t"
    total=0 #declaring variable total=0 so sum starts calculating from 0.
    
    print("Report Types include All items (""A"") or Total Only (""T"")")
    report_type=input("Choose a report type(""A"" or ""T""): ")
    
    #If all report - Items and Total.
    if report_type.lower()=="a":
        print("Input an integer to add to the total or ""Q"" to quit")
        while report_type.lower()=="a":
            if report_type.lower()=="a":
                intq=input("Enter an integer or ""Q"": ")
                if intq.isdigit()==True:
                    intqlog.append(int(intq)) #append/add the integer keyed in into the array - appending into array
                    total+=int(intq) #calculates the total - adds each integer keyed in up and stores it into total

                elif intq.lower().startswith("q"):
                    print("Items")
                    print("\n".join(str(intq) for intq in intqlog)) #uses the built in join function to display each individual array without , and \n for new line
                    print("\nTotal\n")
                    print(total)
                    break
                else:
                    print(intq,"is an invalid input")
            else:
                break
    
    #same codes as above but replacing intqlog with inttlog as well as removing Items code part, only showing total
    elif report_type.lower()=="t":
        print("Input an integer to add to the total or ""Q"" to quit")
        while report_type.lower()=="t":
            if report_type.lower()=="t":
                intt=input("Enter an integer or ""Q"": ")
                if intt.isdigit()==True:
                    inttlog.append(int(intt))
                    total+=int(intt)

                elif intt.lower().startswith("q"):
                    print("\nTotal\n")
                    print(total)
                    break
                else:
                    print(intt,"is an invalid input")
            else:
                break
    else:
        pass
adding_report()