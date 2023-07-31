# -*- coding: utf-8 -*-
# @Time    : 2023/6/22 12:39
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : classes_num.py
# @Software: PyCharm
# @Comment : 统计每个颜色标签的数量以及对应的correct，wrong和none的数量
# 'E:\\helmetcase\\newYOLO2\\newYOLO2\\newYOLO2\\labels'
# import os
#
# classes = {'blue': 0, 'white': 1, 'yellow': 2, 'red': 3, 'none': 4, 'correct': 5, 'person': 6, 'orange': 7, 'wrong': 8}
# target_classes = {'blue': 0, 'white': 1, 'yellow': 2, 'red': 3, 'orange': 7}
#
# def count_labels(folder_path):
#     """
#     统计指定文件夹下各个类别和颜色标签的标注数量，并返回一个字典。
#     """
#     label_count = {cls: 0 for cls in classes.keys()}
#     color_count = {color: {'correct': 0, 'wrong': 0} for color in target_classes.keys()}
#
#     for file_name in os.listdir(folder_path):
#         if not file_name.endswith('.txt'):
#             continue
#         file_path = os.path.join(folder_path, file_name)
#         with open(file_path, 'r') as f:
#             lines = f.readlines()
#             for line in lines:
#                 values = line.strip().split()
#                 cls_code = int(values[0])
#                 cls = list(classes.keys())[list(classes.values()).index(cls_code)]
#                 if cls in classes.keys():
#                     label_count[cls] += 1
#                     if len(values) > 5 and cls == 'person':
#                         color_code = int(values[5])
#                         color = list(target_classes.keys())[list(target_classes.values()).index(color_code)]
#                         if color in target_classes.keys():
#                             if color == 'wrong' or color == 'correct':
#                                 if values[6] == 'correct':
#                                     color_count[color]['correct'] += 1
#                                 else:
#                                     color_count[color]['wrong'] += 1
#
#     return label_count, color_count
#
# yolo_folder = 'E:\\helmetcase\\newYOLO2\\newYOLO2\\newYOLO2'
# folders = ['train', 'val', 'test']
#
# for folder in folders:
#     image_folder = os.path.join(yolo_folder, 'images', folder)
#     label_folder = os.path.join(yolo_folder, 'labels', folder)
#     label_count, color_count = count_labels(label_folder)
#     print(f"Folder: {folder}")
#     for cls in classes.keys():
#         count = label_count[cls]
#         print(f"{cls}: {count}")
#     print("Wrong/Correct:")
#     for cls in target_classes.keys():
#         wrong_count = color_count[cls]['wrong']
#         correct_count = color_count[cls]['correct']
#         print(f"{cls} Wrong: {wrong_count}, Correct: {correct_count}")
#     print()

'''
import os
import xml.etree.ElementTree as ET

# 颜色标签列表
color_list = ['red', 'orange', 'blue', 'white', 'yellow']

# 定义一个字典用于存储结果
result = {}
for color in color_list:
    result[color] = {'correct': 0, 'wrong': 0}

# 遍历xml文件夹中的所有xml文件
xml_folder_path = 'E:\\helmetcase\\yolo2voc\\test'
for file_name in os.listdir(xml_folder_path):
    # 打开xml文件
    xml_file_path = os.path.join(xml_folder_path, file_name)
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 遍历每个对象
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
                result[color][name] += 1

# 输出结果
for color, counts in result.items():
    total_count = counts['correct'] + counts['wrong']
    print(f'{color}: Total={total_count}, Correct={counts["correct"]}, Wrong={counts["wrong"]}')
'''
import os
import xml.etree.ElementTree as ET

# 颜色标签列表
color_list = ['red', 'orange', 'blue', 'white', 'yellow']

# 定义一个字典用于存储结果
result = {}
for color in color_list:
    result[color] = {'correct': 0, 'wrong': 0}

# 浏览三个文件夹: test_xml, train_xml, val_xml
xml_folders = ['train_xml', 'val_xml', 'test_xml']
#base_folder_path = 'E:\\helmetcase\\yolo2voccase1'  # 修改基础文件夹路径
base_folder_path = 'E:\\helmetcase\\VOC4_labels'

for xml_folder_name in xml_folders:
    # 构建当前文件夹路径
    xml_folder_path = os.path.join(base_folder_path, xml_folder_name)

    # 输出当前文件夹名称
    print(f"Folder: {xml_folder_name}")

    # 遍历当前文件夹中的所有xml文件
    for file_name in os.listdir(xml_folder_path):
        # 打开xml文件
        xml_file_path = os.path.join(xml_folder_path, file_name)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 遍历每个对象
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
                    result[color][name] += 1

    # 输出当前文件夹的结果
    for color, counts in result.items():
        total_count = counts['correct'] + counts['wrong']
        print(f'{color}: Total={total_count}, Correct={counts["correct"]}, Wrong={counts["wrong"]}')

    # 重置结果字典
    result = {}
    for color in color_list:
        result[color] = {'correct': 0, 'wrong': 0}

    print()  # 打印空行，以区分不同文件夹的结果