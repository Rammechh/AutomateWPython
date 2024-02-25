with open('files/Merge/merged.csv', 'r') as file:
  content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'

with open('files/Merge/merged.csv', 'w') as file:
  file.writelines(content)