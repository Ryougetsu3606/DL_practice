import os
with open('test.txt', 'r', encoding='utf-8') as file:
    file_content = file.read()
print("hello, {}". format(file_content))