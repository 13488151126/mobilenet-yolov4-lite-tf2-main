import os
import random

xmlfilepath = "oria"
saveBasePath = "ImageSets\\Main\\"

trainval_percent = 1.0
train_percent = 1.0

temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("traub suze", tr)
ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()


import xml.etree.ElementTree as ET
from os import getcwd

sets = ['train', 'val', 'test']

classes = ["car", "people"]


def convert_annotation(image_id, list_file):
    in_file = open('oria/%s.xml' % image_id, encoding='utf-8')
    tree = ET.parse(in_file)

    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') is not None:
            difficult = obj.find('difficult').text

        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


wd = getcwd()

for image_set in sets:
    image_ids = open('ImageSets/Main/%s.txt' % image_set).read().strip().split()
    list_file = open('xdl_%s.txt' % image_set, 'w')
    for image_id in image_ids:
        list_file.write('C:/Users/sunhaotian/Desktop/xdl/img/ori/%s.jpg' % image_id)
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()
