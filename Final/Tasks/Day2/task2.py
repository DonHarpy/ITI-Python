num =int(input("Enter a number: "))
bigList=[]
for i in range(1, num+1):
     smalLists=[]
     for j in range(1,num+1):
        smalLists.append(f"{i*j}")
        if i == j:
            break
     bigList.append(smalLists)
print(bigList)
        
        