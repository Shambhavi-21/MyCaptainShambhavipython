n=(int(input("enter a number:")))
t1=0
t2=1
nextterm=t2
print(t1)
print(t2)
i=1
while i<=n:
    print(nextterm," ")
    i+=1
    t1,t2=t2,nextterm
    nextterm=t1+t2
print()
       
           
