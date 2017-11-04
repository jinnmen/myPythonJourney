# review and run example using \n (new line)
print("Hello world!\nI am formating print!")

# review and run code using \t (tab)
student_age=17
student_name="Hiroto Yamaguchi"
print("STUDENT NAME\t\tAGE")
print(student_name,'\t' + str(student_age))

# review and run code
# using \" and \' (escaped quotes)
print ("\"quotes in quotes\"")
print ("I\'ve said \"save your notebook,\" so let\'s do it!")

#using \\ (escaped backslash)
print("for a newline use \\n")

#Task 1
# [ ] print "\\\WARNING!///"
print("\\\\\\\WARNING!////")

# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print("\"What's that?\" isn\'t a specific question")

# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("One\tTwo\tThree\nFour\tFive\tSix")

word1="pre"

def pre_word():
    word_pre=input("enter any word")
   
    if word_pre.isalpha()==True:
        if word1 in word_pre.lower():
            print("true")
        else:
            print("false")
    else:
        print("False")
    return

pre_word()