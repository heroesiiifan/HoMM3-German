#!/usr/bin/env python3

from zipfile import ZipFile
import zipfile
import os
from os.path import basename

zipObj = ZipFile('_out/HoMM3DE_source.zip', 'w', zipfile.ZIP_STORED)
folder = os.getcwd()
for foldername, subfolders, filenames in os.walk(folder):
    if foldername == folder:
        archive_folder_name = ''
    else:
        archive_folder_name = os.path.relpath(foldername, folder)
    
    #Filter Folder
    if archive_folder_name.startswith(".git"): continue
    if archive_folder_name.startswith("_out"): continue
    if archive_folder_name.startswith("_tmp"): continue
    #if archive_folder_name.startswith("todo"): continue
    if archive_folder_name.startswith("extra_files"): continue
    if archive_folder_name.startswith("working_files"): continue
    if archive_folder_name.endswith("additional"): continue
    if archive_folder_name.startswith("homm3_files") and not archive_folder_name.endswith("homm3_files"): continue

    if archive_folder_name != '': zipObj.write(foldername, arcname=archive_folder_name)

    for filename in filenames:
        #Filter File
        #if filename == "todo.txt": continue

        zipObj.write(os.path.join(foldername, filename), arcname=os.path.join(archive_folder_name, filename))
zipObj.close()