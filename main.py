import collections
import cv2
import xml.etree.ElementTree as ET
import os
from pathlib import Path
import numpy as np
import random
import numpy as np
import cv2
import xml.etree.ElementTree as ET
import os
from pathlib import Path
import random
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import pyplot as plt, ticker

# 原图片、标签文件、裁剪图片路径
img_path = r'D:\PythonProject\helmets\H_ORANGE'

# def test(array=[]):
#     array.sort(key=None, reverse=False)
#     b = collections.Counter(array)
#     # 转换成字典的格式
#     dic = {number: value for number, value in b.items()}
#     plt.title = "统计数字出现的次数"
#     # 取得key
#     x = [i for i in dic.keys()]
#     y = []
#     # 取得value
#     for i in dic.keys():
#         y.append(dic.get(i))
#
#
#     tick_spacing = 10
#     # 通过修改tick_spacing的值可以修改x轴的密度
#     # 1的时候1到16，5的时候只显示几个
#     fig, ax = plt.subplots(1, 1)
#     ax.plot(x, y)
#     ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
#     plt.show()

if __name__ == '__main__':
    max_h = -361
    min_h = 361
    list=[]
    in_list=[]
    # 声明一个空字典用于储存裁剪图片的类别及其数量
    # 把原图片裁剪后，按类别新建文件夹保存，并在该类别下按顺序编号
    for img_file in os.listdir(img_path):
        if img_file[-4:] in ['.png', '.jpg']:  # 判断文件是否为图片格式
            img_filename = os.path.join(img_path, img_file)  # 将图片路径与图片名进行拼接
            #print("img_filename: " + img_filename)
            img = cv2.imread(img_filename)  # 读取图片
            img_name = (os.path.splitext(img_file)[0])  # 分割出图片名，如“000.png” 图片名为“000”
            HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            w = HSV.shape[0]
            h = HSV.shape[1]
            # x0 = 0
            # x1 = w - 1
            # y0 = 0
            # y1 = h - 1
            for i in range(w):
                for j in range(h):
                    hh = HSV[i, j, 0]
                    list.append(hh)
                    flag=False
                    for z in in_list:
                        if hh==z:
                            flag=True
                            break
                    if flag == False:
                        in_list.append(hh)
    in_list.sort()

    red_x1 = []
    red_y1 = []

    red_x2 = []
    red_y2 = []
    for i in in_list:
        if i <180:
            red_x1.append(i)
            red_y1.append(list.count(i))
        else:
            red_x2.append(i)
            red_y2.append(list.count(i))

        print('h={},该值出现次数{}'.format(i, list.count(i)))
    matplotlib.use('TkAgg')
    # plt.bar(red_x1,red_y1,color = 'orange',width=0.5)
    # plt.bar(red_x2,red_y2,color = 'orange',width=0.5)
    plt.plot(red_x1,red_y1,color='orange')
    plt.plot(red_x2,red_y2,color = 'orange')

    plt.xlabel('val(H_ORANGE)')
    plt.ylabel('total')
    plt.show()
        #print(hh,end=",")
    #求均值
    hh_means = np.mean(list)
    # 求方差
    hh_var=np.var(list)
    #求总体标准差
    # hh_std_1=np.std(list)
    # #求样本标准差
    # hh_std_2=np.std(list,ddof=1)
    print(len(list))
    print(sum(list))
    print("平均值=", hh_means)
    print("方差=", hh_var)
    # print("总体标准差=", hh_std_1)
    # print("样本标准差=", hh_std_2)

    #                 if hh > max_h:
    #                     max_h = hh
    #                 if hh < min_h:
    #                     min_h = hh
    #
    # print("max = " + str(max_h))
    # print("min = " + str(min_h))


    # blue (99,129)
    # yellow (24,32)
    # red (0,10),(170,179)
    # white (75,120)
    # orange (3,17)








