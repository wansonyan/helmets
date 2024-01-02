import matplotlib
import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

# 原图片、标签文件、裁剪图片路径
img_path = r'F:\GraFile\data_hsv(1)\data_hsv\H_YELLOW'

# 双折线图绘制
def two_line(map1, map2, yy):
    # x坐标相同
    x = map1.keys()
    y1 = map1.values()
    y2 = map2.values()

    matplotlib.use('TkAgg')
    fontsize = 12
    plt.plot(x, y1, 'o-', color="#91CC75", label="H")
    for a, b in zip(x, y1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.plot(x, y2, 's-', color="#5470C6", label="HSV-H")
    for a, b in zip(x, y2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=8)
    plt.xlabel("H VALUES OF ORANGE SAFETY HELMET")
    plt.ylabel("FREQUENCY")
    plt.axhline(y=yy)
    plt.legend(loc="best", fontsize=fontsize)
    plt.tight_layout()
    plt.show()

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
    h_map = {}
    s_map = {}
    hsv_map = {}

    # 声明一个空字典用于储存裁剪图片的类别及其数量
    # 把原图片裁剪后，按类别新建文件夹保存，并在该类别下按顺序编号
    for img_file in os.listdir(img_path):
        if img_file[-4:] in ['.png', '.jpg']:  # 判断文件是否为图片格式
            img_filename = os.path.join(img_path, img_file)  # 将图片路径与图片名进行拼接
            # print("img_filename: " + img_filename)
            img = cv2.imread(img_filename)  # 读取图片
            img_name = (os.path.splitext(img_file)[0])  # 分割出图片名，如“000.png” 图片名为“000”
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

                    if h in h_map:
                        h_map[h] += 1
                    else:
                        h_map[h] = 1

                    if s in s_map:
                        s_map[s] += 1
                    else:
                        s_map[s] = 1

                    hsv_key = '(' + h + ', ' + s + ', ' + v + ')'
                    if hsv_key in hsv_map:
                        hsv_map[hsv_key] += 1
                    else:
                        hsv_map[hsv_key] = 1

    # print(h_map)
    print(s_map)
    # print(hsv_map)

    # 按出现频次从大到小排序，取前80%
    s_map = set_rank(s_map)
    s_threshold = pixel_total * 0.81
    s_count = 0
    hsv_count = 0

    s_final_map = {}
    for key in h_map:
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
        if hsv_count >= hsv_threshold:
            break

    # HSV中取出S
    hsv_s_map = {}
    hsv_s_total = 0
    for key in hsv_final_map:
        hsv_count = hsv_final_map[key]
        hsv_s_total += hsv_count
        start = key.find(',')
        end = key.rfind(',')
        s_key = key[start + 2:end].strip()
        if s_key in hsv_s_map:
            hsv_s_map[s_key] += hsv_count
        else:
            hsv_s_map[s_key] = hsv_count

    # HSV-S按频次从大到小排序，并取前90%
    hsv_s_maphsv_s_map = set_rank(hsv_s_map)
    hsv_s_threshold = hsv_s_total * 0.9
    hsv_s_final_map = {}
    for key in hsv_s_map:
        hsv_count += hsv_s_map[key]
        hsv_s_final_map[key] = hsv_s_map[key]
        if hsv_count >= hsv_s_threshold:
            break

    print(hsv_s_final_map)
    # 将hsv_s_final_map中的键转换为整数类型
    s_values = [int(s) for s in hsv_s_final_map.keys()]

    # 查找最小值和最大值之间的有效值
    valid_s_values = []
    min_s = min(s_values)
    max_s = max(s_values)

    for s in range(min_s, max_s + 1):
        if str(s) in hsv_s_final_map:
            valid_s_values.append(s)

    if valid_s_values:
        min_valid_s = min(valid_s_values)
        max_valid_s = max(valid_s_values)
        print("HSV-S范围：{} - {}".format(min_valid_s, max_valid_s))
    else:
        print("在HSV-S范围内没有找到有效值。")