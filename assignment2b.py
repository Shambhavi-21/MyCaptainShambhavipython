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
 