# -*- coding: utf-8 -*-
# @Time    : 2023/12/29 18:19
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : hsv_v.py.py
# @Software: PyCharm 
# @Comment :
import matplotlib
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np


# 原图片、标签文件、裁剪图片路径
img_path = r'F:\GraFile\data_hsv(1)\data_hsv\H_ORANGE'


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
    v_map = {}
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

                    if v in v_map:
                        v_map[v] += 1
                    else:
                        v_map[v] = 1

                    hsv_key = '(' + h + ', ' + s + ', ' + v + ')'
                    if hsv_key in hsv_map:
                        hsv_map[hsv_key] += 1
                    else:
                        hsv_map[hsv_key] = 1
    print(v_map)
    print(hsv_map)

    # 按出现频次从大到小排序，取前80%
    v_map = set_rank(v_map)
    v_threshold = pixel_total * 0.81
    v_count = 0
    hsv_count = 0

    v_final_map = {}
    for key in v_map:
        v_count += v_map[key]
        v_final_map[key] = v_map[key]
        if v_count >= v_threshold:
            break

    # 按出现频次从大到小排序，取前90%
    hsv_map = set_rank(hsv_map)
    hsv_threshold = pixel_total * 0.9
    hsv_final_map = {}
    for key in hsv_map:
        hsv_count += hsv_map[key]
        hsv_final_map[key] = hsv_map[key]
        if hsv_count >= v_threshold:
            break

    hsv_v_map = {}
    hsv_v_total = 0

    for key in hsv_final_map:
        hsv_count = hsv_final_map[key]
        hsv_v_total += hsv_count
        start = key.find(',') + 1
        end = key.find(',', start + 1)
        v_key = key[start:end]

        if v_key in hsv_v_map:
            hsv_v_map[v_key] += hsv_count
        else:
            hsv_v_map[v_key] = hsv_count

    # HSV-V按频次从大到小排序，并取前90%
    hsv_v_map = set_rank(hsv_v_map)
    hsv_v_threshold = hsv_v_total * 0.9
    hsv_v_final_count = 0
    hsv_v_final_map = {}
    for key in hsv_v_map:
        hsv_v_final_count += hsv_v_map[key]
        hsv_v_final_map[key] = hsv_v_map[key]
        if hsv_v_final_count >= hsv_v_threshold:
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
    v_final_pixel_total = 0
    hsv_v_final_pixel_total = 0
    for key in v_final_map:
        if key not in hsv_v_final_map:
            hsv_v_final_map[key] = 0
        else:
            v_final_pixel_total += v_final_map[key]

    for key in hsv_v_final_map:
        if key not in v_final_map:
            v_final_map[key] = 0
        else:
            hsv_v_final_pixel_total += hsv_v_final_map[key]

    # 按键值V排序
    v_final_map = set_rank(v_final_map, 0)
    hsv_s_final_map = set_rank(hsv_v_final_map, 0)
    print("零填充-键值排序")
    print(v_final_map)
    print(hsv_v_final_map)


    v_values = [int(key) for key in v_final_map.keys()]
    v_min = min(v_values)
    v_max = max(v_values)

    print("V 范围：", v_min, "到", v_max)