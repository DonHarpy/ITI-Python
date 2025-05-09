x =input("enter your word: ").lower()
v = ['a', 'e', 'i', 'o', 'u']
count = 0	
for i in x:
    if i in v:
        count += 1
print("Number of vowels in the word is: ", count)