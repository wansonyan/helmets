# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 17:45
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : labelNum.py
# @Software: PyCharm 
# @Comment : 

import xml.dom.minidom
import os, sys
import matplotlib.pyplot as plt
import  numpy as np
import cv2
rootdir = r"E:\\helmetcase\\ANN"
#rootdir = r"E:\\helmetcase\\AAAtest\\white_test"
doc_xml = os.listdir(rootdir)
print('num_anno', len(doc_xml))
classes_list = []
num_label = {}
for i in range(0, len(doc_xml)):
    path = os.path.join(rootdir, doc_xml[i])
    if os.path.isfile(path):
        # 打开xml文档
        path = open(path, encoding='utf-8')
        dom = xml.dom.minidom.parse(path)
        # 得到dom元素的label
        root = dom.documentElement
        label = dom.getElementsByTagName('name')
        for i in range(len(label)):
            c1 = label[i]
            class_name = c1.firstChild.data
            # 列表中不存在则存入列表
            if classes_list.count(class_name) == 0:
                classes_list.append(class_name)
                num_label[class_name] = 0
            num_label[class_name] += 1
print('num_classes', len(classes_list))
print('num_label', num_label)
#这里需要修改！！！！！！！！！！！！！
print('all object',23840)

num = list(num_label.values())
num=np.array(num)
num=num/23840
np.set_printoptions(suppress=True,precision=4)
print(num)


#plt.bar(range(len(num_label.keys())), num_label.values(), color='skyblue', tick_label=num_label.keys())