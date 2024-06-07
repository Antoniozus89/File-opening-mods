from pprint import pprint

file_name = 'Homework.txt'
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)
