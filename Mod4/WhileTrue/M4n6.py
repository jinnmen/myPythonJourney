print("The new line character is "+'"'+'\\'+ 'n' + '"')

print('"That\'s how we escape!"')

# 1       one
# 22      two
# 333     three

print("1\tone\n22\ttwo\n333\tthree")

def quote_me():
    
    keyin=input("Key in something: ")
    if keyin.startswith('"') ==True:
        print("'"+keyin+"'")
    else:
        print("\""+keyin+"\"")
    return

quote_me()