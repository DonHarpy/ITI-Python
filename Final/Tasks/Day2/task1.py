list = []
for i in range(5):
    num = input("Enter a number: ")
    if num.isnumeric():
        list.append(num)
        
print(list)
sorted_list = sorted(list)
reversed_list = sorted(list, reverse=True)
print("Sorted list:", sorted_list)
print("Reversed list:", reversed_list)