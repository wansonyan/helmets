# -*- coding: utf-8 -*-
# @Time    : 2023/9/9 16:12
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : select_filenames.py
# @Software: PyCharm 
# @Comment :
import os
import shutil

# 指定要选择的文件名列表
selected_filenames = ['JJB00005.xml', 'JJB00007.xml', 'JJB00007.xml', 'JJB00008.xml', 'JJB00008.xml', 'JJB00019.xml', 'JJB00019.xml', 'JJB00025.xml', 'JJB00034.xml', 'JJB00035.xml', 'JJB00041.xml', 'JJB00044.xml', 'JJB00044.xml', 'JJB00074.xml', 'JJB00075.xml', 'JJB00084.xml', 'JJB00087.xml', 'JJB00088.xml', 'JJB00091.xml', 'JJB00092.xml', 'JJB00093.xml', 'JJB00094.xml', 'JJB00097.xml', 'JJB00098.xml', 'JJB00100.xml', 'JJB00101.xml', 'JJB00103.xml', 'JJB00105.xml', 'JJB00107.xml', 'JJB00110.xml', 'JJB00110.xml', 'JJB00120.xml', 'JJB00120.xml', 'JJB00122.xml', 'JJB00124.xml', 'JJB00126.xml', 'JJB00128.xml', 'JJB00131.xml', 'JJB00134.xml', 'JJB00136.xml', 'IMG_0574_2.xml', 'IMG_0576_3.xml', 'IMG_0586_2.xml', 'IMG_0588_1.xml', 'IMG_0591_1.xml', 'IMG_0592_1.xml', 'IMG_0629_2.xml', 'IMG_0658_1.xml']

# 指定源文件夹和目标文件夹
source_folder = "E:\\helmetcase\\newcase4test_voc\\newcase4test\\labels\\train_xml"
target_folder = "E:\\helmetcase\\newcase4test_voc\\newcase4test\\labels\\test_xml"

# 确保目标文件夹存在
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹中的文件
for filename in os.listdir(source_folder):
    # 如果文件名在所选文件名列表中，将其移动到目标文件夹
    if filename in selected_filenames:
        source_file = os.path.join(source_folder, filename)
        target_file = os.path.join(target_folder, filename)
        shutil.move(source_file, target_file)
        print(f"{filename} moved to {target_folder}")