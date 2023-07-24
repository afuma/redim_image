
import sys
import os
from PIL import Image

def resize_images(folder_path_src, percentage):
    extensions = [".jpg", ".JPG", ".jpeg", ".png"]
    folder_path_dst = folder_path_src + "/redim/"
    if not os.path.exists(folder_path_dst):
        os.makedirs(folder_path_dst)

    for filename in os.listdir(folder_path_src):
        file_path_src = os.path.join(folder_path_src, filename)
        file_path_dst = os.path.join(folder_path_dst, filename)
        file_extension = os.path.splitext(filename)[1]

        if os.path.isfile(file_path_src) and file_extension in extensions:
            with Image.open(file_path_src) as img:
                width, height = img.size
                new_width = int(width * percentage / 100)
                new_height = int(height * percentage / 100)
                
                resized_img = img.resize((new_width, new_height))
                resized_img.save(file_path_dst)

if __name__ == "__main__":
    folder_path_src = os.getcwd()
    percentage = 35
    resize_images(folder_path_src, percentage)
