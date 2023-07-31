# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 21:44
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : label_num.py
# @Software: PyCharm 
# @Comment : 统计xml文件中的各个标签数量

import os
import xml.etree.ElementTree as ET

# 指定 XML 文件所在的文件夹路径
#xml_folder = 'E:\\helmetcase\\newVOC2\\ANN' #F:/GraFile/helmet/DATA0109/ANN
xml_folder = 'E:\\helmetcase\\newredcase1\\case1\\ANN'
# 定义标签列表
labels = ['blue','white','yellow','red','none','correct','person','orange','wrong']

# 定义标签计数器
label_count = {label: 0 for label in labels}

# 遍历 XML 文件夹中的所有 XML 文件
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        # 解析 XML 文件并获取 root 元素
        xml_path = os.path.join(xml_folder, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        # 遍历 root 元素下的所有 object 元素
        for obj in root.findall('object'):
            # 获取当前 object 元素的 label 元素
            label = obj.find('name').text
            # 如果当前 label 在定义的标签列表中，则增加对应计数器的值
            if label in labels:
                label_count[label] += 1

# 输出每个标签及其对应的数量
for label, count in label_count.items():
    print(f'{label}: {count}')

