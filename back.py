import os
import shutil

source = input("Enter source folder : ")
destination = input("Enter destination folder : ")

source = source+'/'
destination = destination+'/'

list_of_files = os.listdir(source)
for file in list_of_files :
    shutil.copy((source+file),destination)