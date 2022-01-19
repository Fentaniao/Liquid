# A program designed to deploy README.md file

import os
import re

# 设定目录
print('Turn to Root directory...')
os.chdir('..\\')
root_dir = os.getcwd() + '\\'
target_dir = root_dir + '\\release\\'
print('<< Root directory: ' + root_dir)
print('<< Target directory: ' + target_dir)



print('>> Processing README.md: ')
os.popen('copy 1.txt.py 2.txt.py')


    combine_import(file_name, target_dir + file_name)


with open(target_file_path, 'a', encoding='UTF-8') as target_f:
    lines = re.sub(r"@import '(.*)';", "", lines)
    target_f.write(lines + '\n\n')