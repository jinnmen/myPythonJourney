intqbase=0
intqsum=0
#intqlog=[]

def adding_report():
    intqlog=[]
    intqlogstr=str(''.join(intqlog))
    sumq=sum(int(intqlogstr))
    
    print("Report Types include All items (""A"") or Total Only (""T"")")
    report_type=input("Choose a report type(""A"" or ""T""): ")
    
    if report_type=="A":
        print("Input an integer to add to the total or ""Q"" to quit")
        while True:
            if report_type=="A":
                intq=input("Enter an integer or ""Q"": ")
                if intq.isdigit()==True:
                    #intqsum=int(intqbase)+int(intq)
                    intqlog.append(intq)
                    #intq=input("Enter an integer or ""Q"": ")

                elif intq.lower().startswith("q"):
                    print("Items")
                    print("\n".join(intqlog))
                    print("\nTotal\n",sumq)

                    break
                else:
                    print(intq,"is an invalid input")
            else:
                break
adding_report()