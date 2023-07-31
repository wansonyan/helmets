# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 21:32
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : img_xml.py
# @Software: PyCharm 
# @Comment : 删除图片对应多余的xml文件或者img文件
import os

#指定 XML 文件所在的文件夹路径
xml_folder = 'E:\\helmetcase\\newVOC2case1\\ANN'

#指定图像文件所在的文件夹路径
image_folder = 'E:\\helmetcase\\newVOC2case1\\IMG'

# # 获取 XML 文件夹中的所有 XML 文件名
# xml_files = [f for f in os.listdir(xml_folder) if f.endswith('.xml')]
#
# # 遍历 XML 文件夹中的所有 XML 文件
# for xml_file in xml_files:
#     # 获取 XML 文件对应的图像文件名
#     image_file = os.path.splitext(xml_file)[0] + '.jpg'
#     # 拼接出图像文件的完整路径
#     image_path = os.path.join(image_folder, image_file)
#     # 如果图像文件不存在，则删除该 XML 文件
#     if not os.path.exists(image_path):
#         xml_path = os.path.join(xml_folder, xml_file)
#         os.remove(xml_path)
#         print(f'Removed {xml_file}')

# import os
#
# # # 指定 XML 文件所在的文件夹路径
# # xml_folder = '/path/to/xml/folder'
# #
# # # 指定图像文件所在的文件夹路径
# # image_folder = '/path/to/image/folder'
#
#获取图像文件夹中的所有图像文件名
xml_files = [f for f in os.listdir(xml_folder) if f.endswith('.xml')]
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

# 遍历 XML 文件列表
for xml_file in xml_files:
    # 获取 XML 文件对应的图像文件名
    image_file = os.path.splitext(xml_file)[0] + '.jpg'
    # 构建图像文件的完整路径
    image_path = os.path.join(image_folder, image_file)
    # 如果图像文件不存在，则输出该 XML 文件名
    if not os.path.exists(image_path):
        print(f'Extra XML file found: {xml_file}')


