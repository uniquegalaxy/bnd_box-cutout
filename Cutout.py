import numpy as np
from PIL import ImageOps, ImageEnhance, ImageFilter, Image, ImageDraw
import random
import os
from xml.etree import ElementTree as ET

class augment:
    def __init__(self,box_x_min,box_x_max,box_y_min,box_y_max,proportion_max=0.6,proportion_min=0.4):
        self.box_x_min = int(box_x_min)
        self.box_x_max = int(box_x_max)
        self.box_y_min = int(box_y_min)
        self.box_y_max = int(box_y_max)
        self.max = proportion_max
        self.min = proportion_min

    def Cutout (self,img):
        v = self.get_level()
        x0 = np.random.uniform(self.box_x_min,self.box_x_max)
        y0 = np.random.uniform(self.box_y_min,self.box_y_max)

        x0 = int(max(0, x0 - v / 2.))
        y0 = int(max(0, y0 - v / 2.))
        x1 = min(int(self.box_x_max), x0 + v)
        y1 = min(int(self.box_y_max), y0 + v)

        xy = (x0, y0, x1, y1)
        color = (0, 0, 0)
        img = img.copy()
        ImageDraw.Draw(img).rectangle(xy, color)
        return img

    def get_level(self):
        v  = random.random()
        if v<self.min:
            v = self.min
        elif v>self.max:
            v = self.max
        level = int(v * (self.box_x_max-self.box_x_min+self.box_y_max-self.box_y_min))
        return level

def load_dir(path):
    file_dic = []
    name_dic = os.listdir(path)
    for i in name_dic:
        file_path_element = os.path.join(path,i)
        file_dic.append(file_path_element)
    return file_dic

def read_xml(xml):
    tree = ET.parse(str(xml))
    root = tree.getroot()
    bndbox_x_min = root.find('object').find('bndbox').find('xmin')
    bndbox_x_max = root.find('object').find('bndbox').find('xmax')
    bndbox_y_min = root.find('object').find('bndbox').find('ymin')
    bndbox_y_max = root.find('object').find('bndbox').find('ymax')
    return bndbox_x_min.text,bndbox_x_max.text,bndbox_y_min.text,bndbox_y_max.text


if __name__ == '__main__':

    #file path
    img_path = r"origin/img/"
    xml_path = r"origin/xml/"
    save_path_img = r"result/img/"
    save_path_xml = r"result/xml/"

    img_dic = load_dir(img_path)
    xml_dic = load_dir(xml_path)
    #The proportion of the cropped part to the annotation frame



    for i,j in zip(img_dic,xml_dic):
        #read bndbox
        bndbox_x_min, bndbox_x_max, bndbox_y_min, bndbox_y_max = read_xml(j)
        img = Image.open(i)

        augment1 = augment(bndbox_x_min, bndbox_x_max, bndbox_y_min, bndbox_y_max,proportion_max = 0.6,proportion_min = 0.4)
        img_augment = augment1.Cutout(img)
        img_augment.save(save_path_img + "Cutout" + os.path.basename(i))
        tree = ET.parse(str(j))
        tree.write(save_path_xml + "Cutout" + os.path.basename(j), encoding="utf-8")



