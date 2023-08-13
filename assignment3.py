def string(string):
    d = dict()
    for key in string:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d
a=input("enter a string:")
print (string(a))

#for the string "Mississippi"
"""def string(string):
    d = dict()
    for key in string:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d
a=input("enter a string:")
print (string("Mississippi))"""