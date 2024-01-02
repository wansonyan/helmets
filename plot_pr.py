# -*- coding: utf-8 -*-
# @Time    : 2023/10/28 10:49
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : plot_pr.py
# @Software: PyCharm 
# @Comment :

import numpy as np
import matplotlib.pyplot as plt
# from pycocotools import mask as maskUtils

# # 从预测结果txt文件中读取预测结果
# def read_predictions(file_path):
#     predictions = []
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             line = line.strip().split()
#             class_index = int(line[0])
#             confidence = float(line[1])
#             bbox = [float(x) for x in line[2:]]
#             predictions.append((class_index, confidence, bbox))
#     return predictions

# # 从标注txt文件中读取标注结果
# def read_annotations(file_path):
#     annotations = []
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             line = line.strip().split()
#             class_index = int(line[0])
#             bbox = [float(x) for x in line[1:]]
#             annotations.append((class_index, bbox))
#     return annotations

# # 将目标按照大小分成不同的组
# def group_objects_by_size(annotations, size_thresholds):
#     size_groups = [[] for _ in range(len(size_thresholds) + 1)]

#     for annotation in annotations:
#         _, bbox = annotation
#         bbox_width = bbox[2] - bbox[0]
#         bbox_height = bbox[3] - bbox[1]
#         bbox_size = min(bbox_width, bbox_height)

#         group_index = -1
#         for i, threshold in enumerate(size_thresholds):
#             if bbox_size <= threshold:
#                 group_index = i
#                 break

#         if group_index == -1:
#             group_index = len(size_thresholds)

#         size_groups[group_index].append(annotation)

#     return size_groups

# # 计算IoU
# def compute_iou(bbox1, bbox2):
#     x1 = max(bbox1[0], bbox2[0])
#     y1 = max(bbox1[1], bbox2[1])
#     x2 = min(bbox1[2], bbox2[2])
#     y2 = min(bbox1[3], bbox2[3])

#     intersection = max(0, x2 - x1) * max(0, y2 - y1)
#     area1 = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1])
#     area2 = (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1])
#     union = area1 + area2 - intersection

#     iou = intersection / (union + 1e-8)
#     return iou

# # 计算精确率和召回率
# def compute_precision_recall(predictions, annotations, confidence_threshold, iou_threshold):
#     tp = [0] * 9  # True Positives
#     fp = [0] * 9  # False Positives
#     fn = [0] * 9  # False Negatives

#     for prediction in predictions:
#         class_index, confidence, bbox = prediction
#         if confidence >= confidence_threshold:
#             # 检测到的目标与标注的目标进行匹配
#             matched = False
#             for annotation in annotations:
#                 ann_class_index, ann_bbox = annotation
#                 if class_index == ann_class_index and compute_iou(bbox, ann_bbox) >= iou_threshold:
#                     matched = True
#                     break
#             if matched:
#                 tp[class_index] += 1
#             else:
#                 fp[class_index] += 1

#     for annotation in annotations:
#         ann_class_index, ann_bbox = annotation
#         # 没有被检测到的目标
#         matched = False
#         for prediction in predictions:
#             class_index, confidence, bbox = prediction
#             if confidence >= confidence_threshold and class_index == ann_class_index and compute_iou(bbox, ann_bbox) >= iou_threshold:
#                 matched = True
#                 break
#         if not matched:
#             fn[ann_class_index] += 1

#     precision = [tp[i] / (tp[i] + fp[i] + 1e-8) for i in range(9)]
#     recall = [tp[i] / (tp[i] + fn[i] + 1e-8) for i in range(9)]

#     return precision, recall

# # 绘制PR曲线
# def plot_pr_curve(precisions, recalls, labels):
#     for precision, recall, label in zip(precisions, recalls, labels):
#         plt.plot(recall, precision, '-o', label=label)
#     plt.xlabel('Recall')
#     plt.ylabel('Precision')
#     plt.title('Precision-Recall Curve')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # 类别标签和其对应的索引
# class_labels = ['blue', 'white', 'yellow', 'red', 'none', 'correct', 'person', 'orange', 'wrong']
# class_indices = list(range(len(class_labels)))

# # 读取预测结果和标注结果
# predictions = read_predictions('/home/rock/yws/yolov7-tiny-test/runs/test/newbase-dp-json2/labels')
# annotations = read_annotations('/home/rock/newdatasets/newbase/labels/test')

# # 设置置信度阈值和IoU阈值
# confidence_threshold = 0.5
# iou_threshold = 0.5

# # 计算精确率和召回率
# precision, recall = compute_precision_recall(predictions, annotations, confidence_threshold, iou_threshold)

# # 绘制PR曲线
# plot_pr_curve([precision], [recall], ['Overall'])

import numpy as np
import matplotlib.pyplot as plt
from pycocotools import mask as maskUtils
import os

# 从预测结果txt文件中读取预测结果
def read_predictions(file_path):
    predictions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            class_index = int(line[0])
            confidence = float(line[1])
            bbox = [float(x) for x in line[2:]]
            predictions.append((class_index, confidence, bbox))
    return predictions

# 从标注txt文件中读取标注结果
def read_annotations(file_path):
    annotations = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().split()
            class_index = int(line[0])
            bbox = [float(x) for x in line[1:]]
            annotations.append((class_index, bbox))
    return annotations

# 将目标按照大小分成不同的组
def group_objects_by_size(annotations, size_thresholds):
    size_groups = [[] for _ in range(len(size_thresholds) + 1)]

    for annotation in annotations:
        _, bbox = annotation
        bbox_width = bbox[2] - bbox[0]
        bbox_height = bbox[3] - bbox[1]
        bbox_size = min(bbox_width, bbox_height)

        group_index = -1
        for i, threshold in enumerate(size_thresholds):
            if bbox_size <= threshold:
                group_index = i
                break

        if group_index == -1:
            group_index = len(size_thresholds)

        size_groups[group_index].append(annotation)

    return size_groups

# 计算IoU
def compute_iou(bbox1, bbox2):
    x1 = max(bbox1[0], bbox2[0])
    y1 = max(bbox1[1], bbox2[1])
    x2 = min(bbox1[2], bbox2[2])
    y2 = min(bbox1[3], bbox2[3])

    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    area1 = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1])
    area2 = (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1])
    union = area1 + area2 - intersection

    iou = intersection / (union + 1e-8)
    return iou

# 计算精确率和召回率
def compute_precision_recall(predictions, annotations, confidence_threshold, iou_threshold):
    tp = [0] * 9  # True Positives
    fp = [0] * 9  # False Positives
    fn = [0] * 9  # False Negatives

    for prediction in predictions:
        class_index, confidence, bbox = prediction
        if confidence >= confidence_threshold:
            # 检测到的目标与标注的目标进行匹配
            matched = False
            for annotation in annotations:
                ann_class_index, ann_bbox = annotation
                if class_index == ann_class_index and compute_iou(bbox, ann_bbox) >= iou_threshold:
                    matched = True
                    break
            if matched:
                tp[class_index] += 1
            else:
                fp[class_index] += 1

    for annotation in annotations:
        ann_class_index, ann_bbox = annotation
        # 没有被检测到的目标
        matched = False
        for prediction in predictions:
            class_index, confidence, bbox = prediction
            if confidence >= confidence_threshold and class_index == ann_class_index and compute_iou(bbox, ann_bbox) >= iou_threshold:
                matched = True
                break
        if not matched:
            fn[ann_class_index] += 1

    precision = [tp[i] / (tp[i] + fp[i] + 1e-8) for i in range(9)]
    recall = [tp[i] / (tp[i] + fn[i] + 1e-8) for i in range(9)]

    return precision, recall

# 绘制PR曲线
def plot_pr_curve(precisions, recalls, labels):
    for precision, recall, label in zip(precisions, recalls, labels):
        plt.plot(recall, precision, '-o', label=label)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

# 绘制PR曲线
def plot_pr_curve(precisions, recalls, labels):
    for precision, recall, label in zip(precisions, recalls, labels):
        plt.plot(recall, precision, '-o', label=label)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.show()

# 读取多个预测结果和标注结果
def read_multiple_predictions(predictions_directory):
    predictions = []
    for file_name in os.listdir(predictions_directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(predictions_directory, file_name)
            prediction = read_predictions(file_path)
            predictions.append(prediction)
    return predictions

def read_multiple_annotations(annotations_directory):
    annotations = []
    for file_name in os.listdir(annotations_directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(annotations_directory, file_name)
            annotation = read_annotations(file_path)
            annotations.append(annotation)
    return annotations

# 设置不同的置信度阈值和IoU阈值
confidence_thresholds = [0.5, 0.6, 0.7]
iou_thresholds = [0.5, 0.6, 0.7]

# 存储精确率和召回率的列表
precisions = []
recalls = []
labels = []

# 读取多个预测结果和标注结果
predictions_directory = 'E:\\helmetcase\\txttest\\pred'
annotations_directory = 'E:\\helmetcase\\txttest\\anno'

predictions = read_multiple_predictions(predictions_directory)
annotations = read_multiple_annotations(annotations_directory)

# 计算每个预测结果和标注结果对应的精确率和召回率
for i, prediction in enumerate(predictions):
    precision, recall = compute_precision_recall(prediction, annotations[i], confidence_thresholds[i], iou_thresholds[i])
    precisions.append(precision)
    recalls.append(recall)
    labels.append(f'Threshold {i+1}')

# 绘制PR曲线
plot_pr_curve(precisions, recalls, labels)
