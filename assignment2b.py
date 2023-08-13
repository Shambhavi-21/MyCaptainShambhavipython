list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    item = int(input())
    list.append(item) 
print(list)
item=0
while item<len(list):
    if list[item]>=0:
        print(list[item]," ")
    item+=1

#for list [12,-7,5,64,-14]
"""list = [12,-7,5,64,-14]
item=0
while item<len(list):
    if list[item]>=0:
        print(list[item]," ")
    item+=1"""

##for list [12,14,-95,3]
"""list = [12,14,-95,3]
item=0
while item<len(list):
    if list[item]>=0:
        print(list[item]," ")
    item+=1"""

 