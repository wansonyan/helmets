# -*- coding: utf-8 -*-
# @Time    : 2023/6/20 17:51
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : newVOC2YOLO.py
# @Software: PyCharm 
# @Comment : 将xml文件转为yolo格式的txt文件，并按比例划分数据集
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
只要新建一个文件夹比如newYOLO，然后修改输入输出的路径。就可以一键生成yolo数据集
前提是你的输入文件夹格式
newVOC
    |--IMG
    |--ANN
'''
output_folder = 'E:\\helmetcase\\newredcase1\\newYOLOcase1'
input_floder = 'E:\\helmetcase\\newredcase1\\case1'
create_dataset_folders(output_folder)
xml_folder = os.path.join(input_floder, "ANN")
img_floder = os.path.join(input_floder, "IMG")
xml_files = get_xml_files(xml_folder)

train, val, test = split_dataset(xml_files, train_ratio, val_ratio, test_ratio)
liebiao = [train, val, test]
wenjian = ["train", "val", "test"]

for i in range(3):
    floder = wenjian[i]
    li = liebiao[i]
    for file in li:
        name = file.split("/")[-1].split(".")[0]
        contant = convert_annotation(file)
        txt_path = os.path.join(output_folder, "labels")
        txt_path = os.path.join(txt_path, floder)
        txt_path = os.path.join(txt_path, name + ".txt")
        with open(txt_path, "w") as f:
            f.write(contant)
        # 27 29 34 37 39 47
        img_out_path = os.path.join(output_folder, "images")
        img_out_path = os.path.join(img_out_path, floder)
        img_out_path = os.path.join(img_out_path, name + ".jpg")

        image_path = os.path.join(img_floder, name + ".jpg")
        shutil.copy(image_path, img_out_path)


