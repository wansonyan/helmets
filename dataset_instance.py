# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 11:10
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : dataset_instance.py
# @Software: PyCharm 
# @Comment :
import os
from xml.etree import ElementTree as ET

def calculate_instance_area(bbox):
    xmin = float(bbox.find('xmin').text)
    ymin = float(bbox.find('ymin').text)
    xmax = float(bbox.find('xmax').text)
    ymax = float(bbox.find('ymax').text)
    width = xmax - xmin
    height = ymax - ymin
    area = width * height
    return area

def count_xml_categories_by_area(folder_path, area_ranges):
    categories = {}
    total_instances = 0  # 统计实例总数
    total_counts = 0  # 不同尺度下统计出来的实例总数
    area_counts = {area_range: 0 for area_range in area_ranges}

    # 遍历文件夹中的每个XML文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            tree = ET.parse(file_path)
            root = tree.getroot()

            # 获取XML文件中的类别和框信息
            for obj in root.findall('object'):
                category = obj.find('name').text
                bbox = obj.find('bndbox')

                # 计算实例的像素面积
                area = calculate_instance_area(bbox)

                # 统计类别及其数量
                if category in categories:
                    categories[category] += 1
                else:
                    categories[category] = 1

                total_instances += 1

                # 根据面积范围统计数量
                for area_range in area_ranges:
                    if area > area_range[0] and area <= area_range[1]:
                        area_counts[area_range] += 1
                        total_counts += 1
                        break

    return categories, area_counts, total_counts, total_instances

folder_path = r'E:\helmetcase\ANN'
area_ranges = [(0, 25**2), (25**2, 46**2), (46**2, 67**2), (67**2, 87**2), (87**2, 108**2), (108**2, 129**2), (129**2, 150**2),
               (150**2, 171**2), (171**2, 192**2), (192**2, 212**2), (212**2, 233**2), (233**2, 254**2), (254**2, 275**2), (275**2, 296**2),
               (296**2, 317**2), (317**2, 337**2), (337**2, 358**2), (358**2, 379**2), (379**2, 400**2), (400**2, 100000000000)]  # 设置不同像素面积范围
categories, area_counts, total_instances, total_counts = count_xml_categories_by_area(folder_path, area_ranges)

# 打印类别及其数量
for category, count in categories.items():
    print(f'类别: {category}, 数量: {count}')

# 打印不同像素面积范围下的数量
for area_range, count in area_counts.items():
    print(f'像素面积范围: {area_range}, 数量: {count}')

# 打印统计实例总数
print(f'实例总数：{total_instances}')

# 打印不同尺度下统计出来的实例总数
print(f'不同尺度下实例总数：{total_counts}')