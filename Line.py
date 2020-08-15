import cv2
from glob import glob 
import numpy as np
import math
import os
import shutil


class Lines:
    def __init__(self,path):
        print("---started finding the line-----")
        self.folder_name_list = list()
        for name in glob(path):
            self.folder_name_list.append([name+"/*-1.ppm", name+"/*-01.ppm"])
        if self.folder_name_list:
            self.line()
        else:
            print("no such file found")

    def find_line(self,cropped_img):
        maxi,length,end = 0,0,0
        for idx,pixel in enumerate(cropped_img):
            if pixel == 255:
                length += 1
            elif pixel == 0 and length > maxi:
                maxi = length
                end = idx-1
            else:
                length = 0
        if length > maxi:
            maxi = length
            end = cropped_img.shape[0]
        return maxi,end

    def find_line_img(self,img):
        start_height = int(img.shape[0]/1.7)
        width,end,height = 0,0,0
        for h in range(start_height, img.shape[0], 1):
            new_maxi, new_end = self.find_line(img[h,:])
            if new_maxi > width:
                width = new_maxi
                end = new_end
                height = h
        return width,end,height

    def line(self):
        for folder in self.folder_name_list:
            for path in folder:
                for file_path in glob(path):
                    print(file_path)
                    folder,img_name = os.path.split(file_path)
                    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    gray = cv2.bitwise_not(gray)
                    bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                                cv2.THRESH_BINARY, 15, -2)
                    kernel = np.ones((3,1),np.uint8)
                    bw = cv2.dilate(bw,kernel,iterations = 1)
                    width,end,height = self.find_line_img(bw)
                    img[height-5:,0:end+10] = [255,255,255]
                    cv2.imwrite(folder+"/1.png", img)
                    print(folder+"/1.png is saved")
                    os.remove(file_path)
