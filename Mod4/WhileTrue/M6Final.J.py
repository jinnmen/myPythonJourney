#Final correct version for test
def adding_report():
    intqlog=[]
    inttlog=[]
    total=0
    
    print("Report Types include All items (""A"") or Total Only (""T"")")
    report_type=input("Choose a report type(""A"" or ""T""): ")
    
    if report_type.lower()=="a":
        print("Input an integer to add to the total or ""Q"" to quit")
        while report_type.lower()=="a":
            if report_type.lower()=="a":
                intq=input("Enter an integer or ""Q"": ")
                if intq.isdigit()==True:
                    intqlog.append(int(intq))
                    total+=int(intq)

                elif intq.lower().startswith("q"):
                    print("Items")
                    print("\n".join(str(intq) for intq in intqlog))
                    print("\nTotal\n")
                    print(total)
                    break
                else:
                    print(intq,"is an invalid input")
            else:
                break
    
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