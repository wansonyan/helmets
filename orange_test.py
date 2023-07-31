# -*- coding: utf-8 -*-
# @Time    : 2023/7/12 10:09
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : orange_test.py
# @Software: PyCharm 
# @Comment : 找出仅有orange的xml文件，打印出文件名
# 颜色标签列表
# import os
# import xml.etree.ElementTree as ET
#
# # 颜色标签列表
# color_list = ['red', 'orange', 'blue', 'white', 'yellow']
#
# # 浏览三个文件夹: test_xml, train_xml, val_xml
# xml_folders = ['test_xml', 'train_xml', 'val_xml']
# base_folder_path = 'E:\\helmetcase\\yolo2voc'
#
# for xml_folder_name in xml_folders:
#     # 构建当前文件夹路径
#     xml_folder_path = os.path.join(base_folder_path, xml_folder_name)
#
#     # 输出当前文件夹名称
#     print(f"Folder: {xml_folder_name}")
#
#     # 遍历当前文件夹中的所有xml文件
#     orange_count = 0
#
#     orange_correct_count = 0
#     orange_wrong_count = 0
#
#     for file_name in os.listdir(xml_folder_path):
#         # 打开xml文件
#         xml_file_path = os.path.join(xml_folder_path, file_name)
#         tree = ET.parse(xml_file_path)
#         root = tree.getroot()
#
#         # 遍历每个对象
#         color_count = {'orange': 0, 'white': 0, 'red': 0, 'blue': 0, 'yellow': 0}
#         for obj in root.findall('object'):
#             name = obj.find('name').text
#
#             # 如果该对象是 correct 或 wrong 标记，则查找对应的颜色标记
#             if name == 'correct' or name == 'wrong':
#                 color = None
#
#                 # 计算 correct 或 wrong 标记的 IoU 值最大的颜色标记
#                 max_iou = 0
#                 for color_obj in root.findall('object'):
#                     color_name = color_obj.find('name').text
#                     if color_name in color_list:
#                         color_bndbox = color_obj.find('bndbox')
#                         xmin = int(color_bndbox.find('xmin').text)
#                         ymin = int(color_bndbox.find('ymin').text)
#                         xmax = int(color_bndbox.find('xmax').text)
#                         ymax = int(color_bndbox.find('ymax').text)
#
#                         # 计算 correct 或 wrong 标记与颜色标记的 IoU 值
#                         bndbox = obj.find('bndbox')
#                         x1 = max(xmin, int(bndbox.find('xmin').text))
#                         y1 = max(ymin, int(bndbox.find('ymin').text))
#                         x2 = min(xmax, int(bndbox.find('xmax').text))
#                         y2 = min(ymax, int(bndbox.find('ymax').text))
#                         intersection = max(0, x2 - x1) * max(0, y2 - y1)
#                         union = (xmax - xmin) * (ymax - ymin) + (int(bndbox.find('xmax').text) - int(bndbox.find('xmin').text)) * (int(bndbox.find('ymax').text) - int(bndbox.find('ymin').text)) - intersection
#                         iou = intersection / union
#
#                         if iou > max_iou:
#                             max_iou = iou
#                             color = color_name
#
#                 # 如果找到了对应的颜色标记，则将正确或错误计数器加一
#                 if color is not None:
#                     color_count[color] += 1
#
#         # 如果只有 orange 颜色标记，则将计数器加一
#         if color_count['orange'] > 0 and color_count['white'] == 0 and color_count['red'] == 0 and color_count['blue'] == 0 and color_count['yellow'] == 0:
#             orange_count += 1
#             print(file_name)
#
#     # 输出仅包含 orange 颜色标记的文件数量
#     print(f"Number of orange-only files: {orange_count}")
#
#     print()  # 打印空行，以区分不同文件夹的结果

import os
import xml.etree.ElementTree as ET

# 颜色标签列表
color_list = ['red', 'orange', 'blue', 'white', 'yellow']

# 浏览三个文件夹: test_xml, train_xml, val_xml
xml_folders = ['test_xml', 'train_xml', 'val_xml']
base_folder_path = 'E:\\helmetcase\\yolo2voc'

for xml_folder_name in xml_folders:
    # 构建当前文件夹路径
    xml_folder_path = os.path.join(base_folder_path, xml_folder_name)

    # 输出当前文件夹名称
    print(f"Folder: {xml_folder_name}")

    # 遍历当前文件夹中的所有xml文件
    orange_count = 0
    orange_correct_count = 0
    orange_wrong_count = 0
    orange_correct_files = []
    orange_wrong_files = []
    for file_name in os.listdir(xml_folder_path):
        # 打开xml文件
        xml_file_path = os.path.join(xml_folder_path, file_name)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 遍历每个对象
        color_count = {'orange': 0, 'white': 0, 'red': 0, 'blue': 0, 'yellow': 0}
        orange_correct = 0
        orange_wrong = 0
        for obj in root.findall('object'):
            name = obj.find('name').text

            # 如果该对象是 correct 或 wrong 标记，则查找对应的颜色标记
            if name == 'correct' or name == 'wrong':
                color = None

                # 计算 correct 或 wrong 标记的 IoU 值最大的颜色标记
                max_iou = 0
                for color_obj in root.findall('object'):
                    color_name = color_obj.find('name').text
                    if color_name in color_list:
                        color_bndbox = color_obj.find('bndbox')
                        xmin = int(color_bndbox.find('xmin').text)
                        ymin = int(color_bndbox.find('ymin').text)
                        xmax = int(color_bndbox.find('xmax').text)
                        ymax = int(color_bndbox.find('ymax').text)

                        # 计算 correct 或 wrong 标记与颜色标记的 IoU 值
                        bndbox = obj.find('bndbox')
                        x1 = max(xmin, int(bndbox.find('xmin').text))
                        y1 = max(ymin, int(bndbox.find('ymin').text))
                        x2 = min(xmax, int(bndbox.find('xmax').text))
                        y2 = min(ymax, int(bndbox.find('ymax').text))
                        intersection = max(0, x2 - x1) * max(0, y2 - y1)
                        union = (xmax - xmin) * (ymax - ymin) + (int(bndbox.find('xmax').text) - int(bndbox.find('xmin').text)) * (int(bndbox.find('ymax').text) - int(bndbox.find('ymin').text)) - intersection
                        iou = intersection / union

                        if iou > max_iou:
                            max_iou = iou
                            color = color_name

                # 如果找到了对应的颜色标记，则将正确或错误计数器加一
                if color is not None:
                    color_count[color] += 1

                # 如果该对象是 orange 颜色标记，且对应的正确或错误标记是 correct，则将 orange_correct 计数器加一，并记录对应的文件名
                if name == 'correct' and color == 'orange':
                    orange_correct += 1
                    orange_correct_files.append(file_name)

                # 如果该对象是 orange 颜色标记，且对应的正确或错误标记是 wrong，则将 orange_wrong 计数器加一，并记录对应的文件名
                if name == 'wrong' and color == 'orange':
                    orange_wrong += 1
                    orange_wrong_files.append(file_name)

        # 如果只有 orange 颜色标记，则将 orange-only 文件数量计数器加一，并统计 orange 对应的文件名列表

        # 如果只有 orange 颜色标记，则将 orange-only 文件数量计数器加一，并统计 orange 对应的文件名列表
        if sum(color_count.values()) == color_count['orange']:
            orange_count += 1
            if orange_correct > 0:
                orange_correct_count += 1
            elif orange_wrong > 0:
                orange_wrong_count += 1

    # 输出 orange-only 文件数量以及 orange-correct 和 orange-wrong 对应的文件名列表
    print(f"Number of orange-only files: {orange_count}")
    print(f"Number of orange-correct files: {orange_correct_count}")
    print(f"Number of orange-wrong files: {orange_wrong_count}")
    print(f"File names of orange-correct files: {orange_correct_files}")
    print(f"File names of orange-wrong files: {orange_wrong_files}")