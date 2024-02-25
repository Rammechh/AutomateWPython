with open('files/removechar.txt', 'r') as file:
    content = file.read()

modifiedContent = content[:-1]

for li in content.splitlines():
    print(li)

# for li in content.split(','):
#     print(li)

with open('files/removechar-new.txt', 'w') as file:
    file.write(modifiedContent)

with open('files/removechar-new.txt', 'r') as file:
    print(file.read())