# -*- coding: utf-8 -*-
# @Time    : 2023/12/29 10:35
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : hsv_s.py.py
# @Software: PyCharm 
# @Comment : F:\GraFile\data_hsv(1)\data_hsv\H_ORANGE

import matplotlib
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np


# 原图片、标签文件、裁剪图片路径
img_path = r'F:\GraFile\data_hsv(1)\data_hsv\H_RED'


# 字典排序，type： 0->按key值排序（升序），1->按value值排序（降序）
def set_rank(a_dict, sort_type=1):
    a_sort_list = sorted(a_dict.items(), key=lambda x: int(x[sort_type]), reverse=sort_type == 1)
    a_sort_dict = {}
    for key, value in a_sort_list:
        a_sort_dict[key] = value
    return a_sort_dict

# 去除字典中频次小于阈值的键值对
def remove_under_threshold(a_dict, th):
    new_map = {}
    for kk in a_dict:
        vv = a_dict[kk]
        if vv >= th:
            new_map[kk] = vv
    return new_map


if __name__ == '__main__':
    pixel_total = 0
    s_map = {}
    hsv_map = {}

    # 声明一个空字典用于储存裁剪图片的类别及其数量
    # 把原图片裁剪后，按类别新建文件夹保存，并在该类别下按顺序编号
    for img_file in os.listdir(img_path):
        if img_file[-4:] in ['.png', '.jpg']:  # 判断文件是否为图片格式
            img_filename = os.path.join(img_path, img_file)  # 将图片路径与图片名进行拼接
            img = cv2.imread(img_filename)  # 读取图片
            img_name = (os.path.splitext(img_file)[0])  # 分割出图片名，如“000.png” 图片名为“000”
            HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h = img.shape[0]
            w = img.shape[1]
            pixel_total += w * h

            for i in range(0, h):
                for j in range(0, w):
                    # pixel_total += 1
                    pixel = HSV[i, j]
                    h = str(HSV[i, j, 0])
                    s = str(HSV[i, j, 1])
                    v = str(HSV[i, j, 2])

                    if s in s_map:
                        s_map[s] += 1
                    else:
                        s_map[s] = 1

                    hsv_key = '(' + h + ', ' + s + ', ' + v + ')'
                    if hsv_key in hsv_map:
                        hsv_map[hsv_key] += 1
                    else:
                        hsv_map[hsv_key] = 1
    print(s_map)
    print(hsv_map)

    # 按出现频次从大到小排序，取前80%
    s_map = set_rank(s_map)
    s_threshold = pixel_total * 0.81
    s_count = 0
    hsv_count = 0

    s_final_map = {}
    for key in s_map:
        s_count += s_map[key]
        s_final_map[key] = s_map[key]
        if s_count >= s_threshold:
            break

    # 按出现频次从大到小排序，取前90%
    hsv_map = set_rank(hsv_map)
    hsv_threshold = pixel_total * 0.9
    hsv_final_map = {}
    for key in hsv_map:
        hsv_count += hsv_map[key]
        hsv_final_map[key] = hsv_map[key]
        if hsv_count >= s_threshold:
            break

    hsv_s_map = {}
    hsv_s_total = 0
    for key in hsv_final_map:
        hsv_count = hsv_final_map[key]
        hsv_s_total += hsv_count
        start = key.find(',') + 1
        end = key.find(',', start)
        s_key = key[start:end]
        if s_key in hsv_s_map:
            hsv_s_map[s_key] += hsv_count
        else:
            hsv_s_map[s_key] = hsv_count

    # HSV-S按频次从大到小排序，并取前90%
    hsv_s_map = set_rank(hsv_s_map)
    hsv_s_threshold = hsv_s_total * 0.9
    hsv_s_final_count = 0
    hsv_s_final_map = {}
    for key in hsv_s_map:
        hsv_s_final_count += hsv_s_map[key]
        hsv_s_final_map[key] = hsv_s_map[key]
        if hsv_s_final_count >= hsv_s_threshold:
            break

    # print("pixel_total = " + str(pixel_total))
    # print("threshold = " + str(s_threshold))
    # print("S初始数据")
    # print(set_rank(s_map))
    # print("S取80%数据")
    # print(set_rank(s_final_map))
    # print("HSV初始数据")
    # print(set_rank(hsv_map))
    # print("HSV取90%数据")
    # print(set_rank(hsv_final_map))
    # print("HSV-S")
    # print(set_rank(hsv_s_map))
    # print("HSV-S取90%")
    # print(set_rank(hsv_s_final_map))

    # 获取S的MAX和MIN
    s_final_pixel_total = 0
    hsv_s_final_pixel_total = 0
    for key in s_final_map:
        if key not in hsv_s_final_map:
            hsv_s_final_map[key] = 0
        else:
            s_final_pixel_total += s_final_map[key]

    for key in hsv_s_final_map:
        if key not in s_final_map:
            s_final_map[key] = 0
        else:
            hsv_s_final_pixel_total += hsv_s_final_map[key]

    # 按键值H排序
    s_final_map = set_rank(s_final_map, 0)
    hsv_s_final_map = set_rank(hsv_s_final_map, 0)
    print("零填充-键值排序")
    print(s_final_map)
    print(hsv_s_final_map)


    s_values = [int(key) for key in s_final_map.keys()]
    s_min = min(s_values)
    s_max = max(s_values)

    print("S 范围：", s_min, "到", s_max)

'''

import cv2
import os

img_path = r'F:\GraFile\data_hsv(1)\data_hsv\H_YELLOW'

def set_rank(a_dict, sort_type=1):
    a_sort_list = sorted(a_dict.items(), key=lambda x: int(x[sort_type]), reverse=sort_type == 1)
    a_sort_dict = {}
    for key, value in a_sort_list:
        a_sort_dict[key] = value
    return a_sort_dict

def remove_under_threshold(a_dict, th):
    new_map = {}
    for kk in a_dict:
        vv = a_dict[kk]
        if vv >= th:
            new_map[kk] = vv
    return new_map


if __name__ == '__main__':
    pixel_total = 0
    s_map = {}
    hsv_map = {}
    hsv_s_map = {}  # 修改此行

    for img_file in os.listdir(img_path):
        if img_file[-4:] in ['.png', '.jpg']:
            img_filename = os.path.join(img_path, img_file)
            img = cv2.imread(img_filename)
            img_name = (os.path.splitext(img_file)[0])
            HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            h = img.shape[0]
            w = img.shape[1]
            pixel_total += w * h

            for i in range(0, h):
                for j in range(0, w):
                    pixel = HSV[i, j]
                    h = str(HSV[i, j, 0])
                    s = str(HSV[i, j, 1])
                    v = str(HSV[i, j, 2])

                    if s in s_map:
                        s_map[s] += 1
                    else:
                        s_map[s] = 1

                    hsv_key = '(' + h + ', ' + s + ', ' + v + ')'
                    if hsv_key in hsv_map:
                        hsv_map[hsv_key] += 1
                    else:
                        hsv_map[hsv_key] = 1

                    if s in hsv_s_map:  # 修改此行
                        hsv_s_map[s] += 1  # 修改此行
                    else:
                        hsv_s_map[s] = 1  # 修改此行

    print(s_map)
    print(hsv_map)

    # 按出现频次从大到小排序，取前80%
    s_map = set_rank(s_map)
    s_threshold = pixel_total * 0.81
    s_count = 0
    hsv_count = 0

    s_final_map = {}
    for key in s_map:
        s_count += s_map[key]
        s_final_map[key] = s_map[key]
        if s_count >= s_threshold:
            break

    # 按出现频次从大到小排序，取前90%
    hsv_map = set_rank(hsv_map)
    hsv_threshold = pixel_total * 0.9
    hsv_final_map = {}
    for key in hsv_map:
        hsv_count += hsv_map[key]
        hsv_final_map[key] = hsv_map[key]
        if hsv_count >= s_threshold:
            break

    hsv_s_map = {}
    hsv_s_total = 0
    for key in hsv_final_map:
        hsv_count = hsv_final_map[key]
        hsv_s_total += hsv_count
        start = key.find(',') + 1
        end = key.find(',', start)
        s_key = key[start:end]
        if s_key in hsv_s_map:
            hsv_s_map[s_key] += hsv_count
        else:
            hsv_s_map[s_key] = hsv_count

    # HSV-S按频次从大到小排序，并取前90%
    hsv_s_map = set_rank(hsv_s_map)
    hsv_s_threshold = hsv_s_total * 0.9
    hsv_s_final_count = 0
    hsv_s_final_map = {}
    for key in hsv_s_map:
        hsv_s_final_count += hsv_s_map[key]
        hsv_s_final_map[key] = hsv_s_map[key]
        if hsv_s_final_count >= hsv_s_threshold:
            break

    print("pixel_total = " + str(pixel_total))
    print("threshold = " + str(s_threshold))
    print("S初始数据")
    print(set_rank(s_map))
    print("S取80%数据")
    print(set_rank(s_final_map))
    print("HSV初始数据")
    print(set_rank(hsv_map))
    print("HSV取90%数据")
    print(set_rank(hsv_final_map))
    print("HSV-S")
    print(set_rank(hsv_s_map))  # 修改此行
    print("HSV-S取90%")
    print(set_rank(hsv_s_final_map))  # 修改此行

    s_final_pixel_total = 0
    hsv_s_final_pixel_total = 0
    for key in s_final_map:
        if key not in hsv_s_final_map:
            hsv_s_final_map[key] = 0
        else:
            s_final_pixel_total += s_final_map[key]

    for key in hsv_s_final_map:
        if key not in s_final_map:
            s_final_map[key] = 0
        else:
            hsv_s_final_pixel_total += hsv_s_final_map[key]

    s_final_map = set_rank(s_final_map, 0)
    hsv_s_final_map = set_rank(hsv_s_final_map, 0)
    print("零填充-键值排序")
    print(s_final_map)
    print(hsv_s_final_map)
'''