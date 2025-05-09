tree = []
height = 5

for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * i
    line = spaces + stars
    tree.append(line)

for i in tree:
    print(i)
