#program to print the extension of a file
filename=input("enter the name of the file:")
dots=filename.split(".")
if(len(dots))>1:
    extension=dots[-1]
    print(extension)
else:
    print("")