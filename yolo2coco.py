# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 16:08
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : yolo2coco.py
# @Software: PyCharm 
# @Comment :
import json
from pycocotools import coco

# 读取YOLO格式数据集中所有图像的标记
data = []
with open('path/to/annotations.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        image_path, *boxes = line.split()
        width, height = get_image_width_and_height(image_path) # 获取图像的宽度和高度
        for box in boxes:
            class_id, x_center, y_center, bbox_width, bbox_height = map(float, box.split(','))
            x1 = (x_center - bbox_width / 2) * width
            y1 = (y_center - bbox_height / 2) * height
            x2 = (x_center + bbox_width / 2) * width
            y2 = (y_center + bbox_height / 2) * height
            data.append({
                'image_id': get_image_id(image_path), # 获取图像文件名或ID
                'category_id': int(class_id),
                'bbox': [x1, y1, x2 - x1, y2 - y1],
                'area': (x2 - x1) * (y2 - y1),
                'iscrowd': 0,
            })

# 创建COCO格式数据集
coco_dataset = {'images': [], 'annotations': [], 'categories': []}
for i, image_path in enumerate(get_all_image_paths()):
    width, height = get_image_width_and_height(image_path) # 获取图像的宽度和高度
    coco_dataset['images'].append({
        'id': i,
        'file_name': get_image_file_name(image_path), # 获取图像文件名
        'width': width,
        'height': height,
    })

# 添加对象类别
for class_id, class_name in enumerate(get_all_class_names()):
    coco_dataset['categories'].append({
        'id': class_id,
        'name': class_name,
        'supercategory': '',
    })

# 添加标记
for ann in data:
    coco_dataset['annotations'].append({
        'id': len(coco_dataset['annotations']),
        'image_id': ann['image_id'],
        'category_id': ann['category_id'],
        'bbox': ann['bbox'],
        'area': ann['area'],
        'iscrowd': 0,
    })

# 将COCO格式数据集保存为JSON文件
with open('path/to/coco.json', 'w') as file:
    json.dump(coco_dataset, file)
