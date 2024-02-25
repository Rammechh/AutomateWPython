from pathlib import Path

pathDir = Path('files/Merge')

merge = ''

for idx,filePath in enumerate(pathDir.iterdir()):
    with open(filePath, 'r') as file:
        content = file.readlines()
        newContent = content[1:]
    if idx == 0:
        content = ''.join(content)
        merge += content + '\n'
    else:
        newContent = ''.join(newContent)
        merge += newContent + '\n'

with open('files/Merge/merged.csv', 'w') as file:
    file.write(merge)
