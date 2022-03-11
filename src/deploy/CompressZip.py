# # 把整个文件夹内的文件打包
import os
import shutil
import time

print('>> Set path: ')
deploy_path = os.getcwd()

src_path = os.path.normpath(deploy_path + '\\..')
root_path = os.path.normpath(src_path + '\\..')
dist_path = os.path.normpath(root_path + '\\dist')
zip_path = os.path.normpath(root_path + '\\liquid.zip')

print('<< Root directory: ' + root_path)
print('<< src directory: ' + src_path)
print('<< dist directory: ' + dist_path)
print('<< Target directory: ' + zip_path)

# Compress
print('\n>> Begin compress... ')

# 读取根目录下文件名
print('<< Files waiting for compressing: ')

for root, dirs, files in os.walk(dist_path):
    print("-path", root)  # 当前目录路径
    print(" dirs", dirs)  # 当前路径下所有子目录
    print(" files", files)  # 当前路径下所有非目录子文件

shutil.make_archive(root_path + '\\liquid', 'zip', dist_path)
print('>> Finish compress.')

# Information
print('\n>> Compress Information: ')
print('<< Time: ' + time.asctime())
file_size = round(os.path.getsize(zip_path) / float(1024 * 1024), 2)
print('<< Zip size: ' + str(file_size) + 'MB')
