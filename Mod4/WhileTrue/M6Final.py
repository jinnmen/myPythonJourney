intqbase="0"
intqsum="0"
intqlog=[]

def adding_report():
    while True:
        report_type=input("Choose a report type(""A"" or ""T""): ")
        print("Report Types include All items (""A"") or Total Only (""T"")")
        if report_type=="A":
            print("Input an integer to add to the total or ""Q"" to quit")
            intq=input("Enter an integer or ""Q"": ")
            if intq.isdigit()==True:
                intqsum=intqbase+intq
                intqlog.append(str(intq))
                intq=input("Enter an integer or ""Q"": ")
            elif intq.lower().startswith("q"):
                print("Items\nintqlog\n\nTotal\nintqsum")
                break
            else:
                print(intq,"is an invalid input")
                
adding_report()