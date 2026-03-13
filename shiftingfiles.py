#Gonna be practicing how to shift files with certain extension from one folder to another, as part of the CodeAlpha Internship tasks.
import os
import shutil as sl

src_folder = r'C:\Studies\internships\CodeAlpha-Projects\Source Folder'
dest_folder = r'C:\Studies\internships\CodeAlpha-Projects\Destination Folder'

#make dest fldr if it doesnt exist
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)
    
'''moving jpg files:
   1. check if extension is .jpg
   2. yes -> giv them a path
   3. use shutil to move them
'''
for filename in os.listdir(src_folder):
    if filename.lower().endswith("jpg"):
        src_path = os.path.join(src_folder,filename)
        dest_path = os.path.join(dest_folder,filename)
        
        sl.move(src_path,dest_path)
        print("Moved:",filename)