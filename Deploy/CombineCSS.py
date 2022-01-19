# A program designed to combine .css files into a single file for distribution

import os
import re


# 迭代写入导入的内容
def combine_import(file_path, target_file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        # 设定目录到当前文件所在的目录
        old_dir = os.getcwd()
        new_dir = os.path.split(file_path)[0]
        # print('Turn to new directory: '+new_dir)
        os.chdir(old_dir + '\\' + new_dir)

        # 读取文件内容
        lines = f.read()
        # print(lines)

        # 正则表达式匹配
        pattern = re.compile(r"@import '(.*)';")
        results = pattern.findall(lines)

        # 迭代打开文件
        if results:
            for imported_file_path in results:
                combine_import(imported_file_path, target_file_path)

                # 恢复目录到导入的文件所在的目录
                os.chdir(old_dir)
                # print('Turn to old directory: '+old_dir)

        # 迭代写入文件
        with open(target_file_path, 'a', encoding='UTF-8') as target_f:
            lines = re.sub(r"@import '(.*)';", "", lines)
            target_f.write(lines + '\n\n')


# 设定目录
print('Turn to Root directory...')
os.chdir('..\\')
root_dir = os.getcwd() + '\\'
target_dir = root_dir + '\\release\\'
print('<< Root directory: ' + root_dir)
print('<< Target directory: ' + target_dir)

# 读取根目录下文件名
print('<< Files in Root directory: ', end='')
fileList = os.listdir('.')
print(fileList)

# 处理根目录下目标css文件
for file_name in fileList:
    os.chdir(root_dir)
    if re.search(r'.*\.css', file_name):
        print('>> Processing ' + file_name + ': ')
        if os.path.exists(target_dir + file_name):
            os.remove(target_dir + file_name)

        combine_import(file_name, target_dir + file_name)
