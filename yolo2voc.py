# -*- coding: utf-8 -*-
# @Time    : 2023/6/24 14:44
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : yolo2voc.py
# @Software: PyCharm 
# @Comment : 从yolo格式的txt文件夹中选出一一对应的xml文件

import random
import shutil
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ['blue', 'white', 'yellow', 'red', 'none', 'correct', 'person', 'orange', 'wrong']

# 定义划分比例
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1


# 检查并创建输出文件夹及其子文件夹
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


# 检查并创建数据集文件夹结构
def create_dataset_folders(output_folder):
    img_folder = os.path.join(output_folder, "images")
    ann_folder = os.path.join(output_folder, "labels")
    create_folder(output_folder)
    create_folder(img_folder)
    create_folder(ann_folder)
    create_folder(os.path.join(img_folder, "train"))
    create_folder(os.path.join(img_folder, "val"))
    create_folder(os.path.join(img_folder, "test"))
    create_folder(os.path.join(ann_folder, "train"))
    create_folder(os.path.join(ann_folder, "val"))
    create_folder(os.path.join(ann_folder, "test"))


# 检查并创建数据集文件夹结构
# create_dataset_folders(output_folder)

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(in_file):  # 转换这一张图片的坐标表示方式（格式）,即读取xml文件的内容，计算后存放在txt文件中。
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    result = ""
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult) == 1:
        #     continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        # print(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        result = result + str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n'
        # out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    return result

# convert_annotation("/home/rock/datasets/newVOC/ANN/HWD00027.xml")


def get_xml_files(folder):
    xml_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".xml"):
                xml_path = os.path.join(root, file)
                xml_files.append(xml_path)
    # train,val,test = split_dataset(xml_files,train_ratio,val_ratio,test_ratio)
    return xml_files


def split_dataset(xml_files, train_ratio, val_ratio, test_ratio):
    random.shuffle(xml_files)
    num_files = len(xml_files)

    num_train = int(num_files * train_ratio)
    num_val = int(num_files * val_ratio)
    num_test = num_files - num_train - num_val

    train_files = xml_files[:num_train]
    val_files = xml_files[num_train:num_train + num_val]
    test_files = xml_files[num_train + num_val:]

    return train_files, val_files, test_files


# 使用示例：
# 检查并创建数据集文件夹结构
'''
只要新建一个文件夹比如newYOLO，然后修改输入输出的路径。就可以一键生成yolo修改后的代码中，我添加了 `create_folder()` 函数来检查并创建输出路径所对应的目录，确保输出目录的存在。我还添加了打印 `txt_path` 的语句，在转换每个 XML 文件时打印生成的路径，方便检查路径是否正确。

以下是完整代码，你可以将其保存为 `newVOC2YOLO.py` 并在终端中运行：

'''

import random
import shutil
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ['blue', 'white', 'yellow', 'red', 'none', 'correct', 'person', 'orange', 'wrong']

# 定义划分比例
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1


# 检查并创建输出文件夹及其子文件夹
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


# 检查并创建数据集文件夹结构
def create_dataset_folders(output_folder):
    img_folder = os.path.join(output_folder, "images")
    ann_folder = os.path.join(output_folder, "labels")
    create_folder(output_folder)
    create_folder(img_folder)
    create_folder(ann_folder)
    create_folder(os.path.join(img_folder, "train"))
    create_folder(os.path.join(img_folder, "val"))
    create_folder(os.path.join(img_folder, "test"))
    create_folder(os.path.join(ann_folder, "train"))
    create_folder(os.path.join(ann_folder, "val"))
    create_folder(os.path.join(ann_folder, "test"))


# 检查并创建数据集文件夹结构
# create_dataset_folders(output_folder)

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(in_file):  # 转换这一张图片的坐标表示方式（格式）,即读取xml文件的内容，计算后存放在txt文件中。
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    result = ""
    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult) == 1:
        #     continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        txt_path = in_file.replace("ANN", "labels").replace(".xml", ".txt")
        print("txt_path:", txt_path)
        with open(txt_path, "w") as f:
            f.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        result = result + str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n'
    return result

# convert_annotation("/home/rock/datasets/newVOC/ANN/HWD00027.xml")


def get_xml_files(folder):
    xml_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".xml"):
                xml_path = os.path.join(root, file)
                xml_files.append(xml_path)
    # train,val,test = split_dataset(xml_files,train_ratio,val_ratio,test_ratio)
    return xml_files


def split_dataset(xml_files, train_ratio, val_ratio, test_ratio):
    random.shuffle(xml_files)
    num_files = len(xml_files)

    num_train = int(num_files * train_ratio)
    num_val = int(num_files * val_ratio)
    num_test = num_files - num_train - num_val

    train_files = xml_files
