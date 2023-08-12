#program to print the extension of a file
filename=input("enter the name of the file:")
dots=filename.split(".")
if(len(dots))>1:
    extension=dots[-1]
if(extension=="py"):
    print("python")
elif(extension=="js"):
    print("javascript")
elif(extension=="txt"):
    print("text")
elif(extension=="c"):
    print("C")
elif(extension=="html"):
    print("HTML")
else:
    print("")
