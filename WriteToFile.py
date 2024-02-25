content = """Multi line string
each enter is taken as next line
"""

with open('files/write.txt', 'w') as file:
    file.write(content)

with open('files/write.txt', 'r') as file:
    print(file.read())