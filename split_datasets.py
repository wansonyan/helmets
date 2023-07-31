# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 14:56
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : split_datasets.py
# @Software: PyCharm 
# @Comment : 根据输入文件夹images和labels的内容将数据集划分为train、val和test三个数据集，并按照7:2:1的比例分配
import os
import random
import shutil

# 设置文件路径和需要的比例
image_dir = "F:/GraFile/helmet/test/images"
label_dir = "F:/GraFile/helmet/test/labels"
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# 获取文件列表
image_files = os.listdir(image_dir)
label_files = os.listdir(label_dir)

# 确保文件名相同
image_files.sort()
label_files.sort()

# 计算数据集大小和每个数据集的大小
num_samples = len(image_files)
num_train = int(num_samples * train_ratio)
num_val = int(num_samples * val_ratio)
num_test = num_samples - num_train - num_val

# 随机选择数据集样本
indices = list(range(num_samples))
random.shuffle(indices)

train_indices = indices[:num_train]
val_indices = indices[num_train:num_train + num_val]
test_indices = indices[-num_test:]

# 拷贝数据集到对应的文件夹中
for idx, dataset_indices in enumerate([train_indices, val_indices, test_indices]):
    if idx == 0:
        output_image_dir = "F:/GraFile/helmet/test/images/train"
        output_label_dir = "F:/GraFile/helmet/test/labels/train"
    elif idx == 1:
        output_image_dir = "F:/GraFile/helmet/test/images/val"
        output_label_dir = "F:/GraFile/helmet/test/labels/val"
    else:
        output_image_dir = "F:/GraFile/helmet/test/images/test"
        output_label_dir = "F:/GraFile/helmet/test/labels/test"

    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    if not os.path.exists(output_label_dir):
        os.makedirs(output_label_dir)

    for i in dataset_indices:
        image_filename = image_files[i]
        label_filename = label_files[i]

        shutil.copy(os.path.join(image_dir, image_filename), os.path.join(output_image_dir, image_filename))
        shutil.copy(os.path.join(label_dir, label_filename), os.path.join(output_label_dir, label_filename))

