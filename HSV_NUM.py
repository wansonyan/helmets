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

if __name__=='__main__':
    dictHsv = {}
    list = []
    in_list = []
    # 声明一个空字典用于储存裁剪图片的类别及其数量
    # 把原图片裁剪后，按类别新建文件夹保存，并在该类别下按顺序编号
    for img_file in os.listdir(img_path):
        if img_file[-4:] in ['.png', '.jpg']:  # 判断文件是否为图片格式
            img_filename = os.path.join(img_path, img_file)  # 将图片路径与图片名进行拼接
            # print("img_filename: " + img_filename)
            img = cv2.imread(img_filename)  # 读取图片
            img_name = (os.path.splitext(img_file)[0])  # 分割出图片名，如“000.png” 图片名为“000”
            HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            #print(HSV.shape)
            for i in range(HSV.shape[0]):
                 for j in range(HSV.shape[1]):
                    #print(type(HSV[i,j]))
                    if str(HSV[i,j].tolist()) not in dictHsv.keys():
                        dictHsv[str(HSV[i,j].tolist())] = 1
                    else:
                        dictHsv[str(HSV[i,j].tolist())] += 1
    for each in dictHsv:
        print(each,":",dictHsv[each])
    # print(dictHsv)
            # print(HSV)
            # w = HSV.shape[0]
            # h = HSV.shape[1]
            # print(w,h)
            # x0 = 0
            # x1 = w - 1
            # y0 = 0
            # y1 = h - 1
            # for i in range(w):
            #     for j in range(h):
            #         print(HSV[w][h])
            #
            #         d = dict(enumerate(HSV.flatten(), 1))

        # print(d)
