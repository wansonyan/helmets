# -*- coding: utf-8 -*-
# @Time    : 2023/7/7 9:57
# @Author  : Ryan
# @PRO_NAME: helmets
# @File    : test.py
# @Software: PyCharm 
# @Comment :
import os

def count_class_instances(folder):
    class_counts = {}
    xml_files = [file for file in os.listdir(folder) if file.endswith(".xml")]

    for xml_file in xml_files:
        xml_path = os.path.join(folder, xml_file)
        with open(xml_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if "<name>" in line:
                    start_index = line.index("<name>") + len("<name>")
                    end_index = line.index("</name>")
                    class_name = line[start_index:end_index]
                    if class_name in class_counts:
                        class_counts[class_name] += 1
                    else:
                        class_counts[class_name] = 1

    return class_counts

test_folder = "E:\\helmetcase\\yolo2voccase1\\test_xml"
train_folder = "E:\\helmetcase\\yolo2voccase1\\train_xml"
val_folder = "E:\\helmetcase\\yolo2voccase1\\val_xml"

test_class_counts = count_class_instances(test_folder)
train_class_counts = count_class_instances(train_folder)
val_class_counts = count_class_instances(val_folder)

print("Test Folder Class Counts:")
for class_name, count in test_class_counts.items():
    print(class_name, count)

print("\nTrain Folder Class Counts:")
for class_name, count in train_class_counts.items():
    print(class_name, count)

print("\nVal Folder Class Counts:")
for class_name, count in val_class_counts.items():
    print(class_name, count)
