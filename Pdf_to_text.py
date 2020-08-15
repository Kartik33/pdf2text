from glob import glob
from pdf2image import convert_from_path, convert_from_bytes
import cv2
import pytesseract as pt
import os
import shutil
from Line import Lines

IMG_FOLDER = "img/"
TXT_FOLDER = "txt/"
class PDF_TO_TEXT:
    
    def __init__(self,path, option, isLine):
        self.path = path
        self.option = option
        self.isLine = isLine
    
    def img_to_text(self, images_path , text_path):
        for fileType in [images_path+"/*.ppm", images_path+"/*.png"]:
            for path in glob(fileType):
                _,image_name = os.path.split(path)
                file_name = image_name.split(".")[0]+".txt"
                t = os.path.join(text_path,file_name)
                img = cv2.imread(path)
                text = pt.image_to_string(img)
                text_file = open(t , "w")
                text_file.write(text)
                text_file.close()
                print(path, "---- converted")
    def convert_single_file(self,path):
        if not os.path.isfile(path):
            print(path, " -------this file was not found-------")
            return
        print("------Conversion started for new file ---------")
        name = os.path.basename(path)
        name_without_ext = name.replace(".pdf","")
        new_img_folder = os.path.join(IMG_FOLDER, name_without_ext)
        new_txt_folder = os.path.join(TXT_FOLDER, name_without_ext)
        version = 1
        while os.path.exists(new_img_folder):
            new_name_without_ext = name_without_ext+str(version)
            new_img_folder = os.path.join(IMG_FOLDER, new_name_without_ext)
            new_txt_folder = os.path.join(TXT_FOLDER, new_name_without_ext)
            version += 1
        try:
            os.makedirs(new_img_folder)
        except PermissionError:
            exit(new_img_folder)
        except FileExistsError as fe:
            shutil.rmtree(new_img_folder)
            os.makedirs(new_img_folder)
            
        try:
            os.makedirs(new_txt_folder)
        except PermissionError:
            exit(new_img_folder)
        except FileExistsError as fe:
            shutil.rmtree(new_txt_folder)
            os.makedirs(new_txt_folder)
        img = convert_from_path(path,output_folder=new_img_folder)
        if self.isLine:
            Lines(new_img_folder)
        self.img_to_text(new_img_folder , new_txt_folder)
        shutil.rmtree(new_img_folder)
        print("Conversion successful for " , path, new_img_folder)
        
    def convert(self):
        if self.option == "file":
            self.convert_single_file(self.path)
        elif self.option == "dir"and os.path.isdir(self.path):
            for path in glob(self.path+"*.pdf"):
                self.convert_single_file(path)
        else:
            exit(self.path+"Dir does not exist")
