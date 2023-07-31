# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 17:59
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : labelTest.py
# @Software: PyCharm 
# @Comment : 
import random
import xml.dom.minidom
import cv2
import numpy as np
from albumentations import (BboxParams, RandomGamma,Compose,Blur,CenterCrop,HueSaturationValue,MotionBlur,Cutout)
import os
import glob
import shutil

def read_xml(path):
    person = 0
    color = 0
    kk = 0
    exp_xml = []
    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    img_name = root.getElementsByTagName("filename")[0]
    exp_xml.append(img_name.childNodes[0].data)
    label = root.getElementsByTagName("name")
    for i in range(label.length):
        if label[i].childNodes[0].data =='person':
            person+=1
        if label[i].childNodes[0].data == 'none':
            person-=1
        if label[i].childNodes[0].data in ['red','yellow','white','blue','orange']:
            color+=1
        if label[i].childNodes[0].data in ['correct','wrong']:
            kk+=1
    exp_xml.append(person)
    exp_xml.append(color)
    exp_xml.append(kk)
    return exp_xml

def get_data(xml_date_path,img_path):

    xml_date = read_xml(xml_date_path)
    return xml_date

def main():

    xml_img_path =r"F:\\GraFile\\DATA0109\\ANN"##图片和标签放同一个文件夹内
    aug_file =r"F:\\GraFile\\DATA0109\\aug"##有问题的存放路径
    for n in range(1):
        num = 0
        print(" 第%d次"%n)
        for xml_name in glob.glob(xml_img_path + '/*.xml'):

            print(" 第%d张图片" % num)
            xml_data = get_data(xml_name, xml_img_path)
            person,color,kk = xml_data[1],xml_data[2],xml_data[3]
            if person!=color or person!=kk or color!=kk:
                from_path = os.path.join(xml_img_path,xml_data[0])
                file = os.path.splitext(xml_data[0])
                front,ext= file
                xml_name = str(front)+'.xml'
                xml_path = os.path.join(xml_img_path,xml_name)
                if os.path.isfile(from_path):
                    shutil.copy(from_path, aug_file)
                    shutil.copy(xml_path,aug_file)
                print(xml_data[0])
if __name__ == "__main__":
    main()