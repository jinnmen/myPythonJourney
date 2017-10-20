# myPythonJourney

https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+4T2017/courseware/372fb285386c4bfe85611cd45a96b325/0384b34b15a445b3ba5a499794cd0575/?child=first

def bird_available():
	bird_types= 'crow robin parrot eagle sandpiper hawk pigeon'
	bname=input("enter a type of bird to search: ")
	print (bname.lower() , "available is: ", bname.lower() in bird_types)

bird_available()

