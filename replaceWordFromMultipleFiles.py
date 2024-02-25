from pathlib import Path

pathDir = Path('files')

for filePath in pathDir.iterdir():
    with open(filePath, 'r') as file:
        content = file.read()
        newContent = content.replace('word', 'Content')
    
    with open(filePath, 'w') as file:
        file.write(newContent)


