from pathlib import Path
p1 = Path('files/abcd.txt')

if p1.exists():
    with open(p1, 'r') as file:
        print(file.read())

# else:
#     with open('files/ghi.txt', 'w') as file:
#         file.write('Content 3')

# print(p1.suffix)

#print(p1.read_text())

# with open(p1, 'r') as file:
#     print(file.read())
        
p2 = Path('files')
print(p2.iterdir())

for item in p2.iterdir():
    print(item.stem)