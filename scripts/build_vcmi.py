#!/usr/bin/env python3

from zipfile import ZipFile
import zipfile
import os
from os.path import basename
import pathlib

zipObj = ZipFile('_out/HoMM3DE_VCMI.zip', 'w', zipfile.ZIP_STORED)

zipObj.write(os.path.join("additional_files/vcmi", "mod.json"), arcname=os.path.join("", "mod.json"))

for filename in os.listdir("additional_files/vcmi/config"):
    zipObj.write(os.path.join("additional_files/vcmi/config", filename), arcname=os.path.join("content/config", filename))

for filename in os.listdir("homm3_files/RoE_de/Maindisk/Maps"):
    zipObj.write(os.path.join("homm3_files/RoE_de/Maindisk/Maps", filename), arcname=os.path.join("content/maps", filename))
for filename in os.listdir("additional_files/translation/campaign/extra"):
    zipObj.write(os.path.join("additional_files/translation/campaign/extra", filename), arcname=os.path.join("content/maps", filename))

for filename in os.listdir("_tmp/fnt"):
    zipObj.write(os.path.join("_tmp/fnt", filename), arcname=os.path.join("content/data", filename))

for filename in os.listdir("_tmp/bmp"):
    zipObj.write(os.path.join("_tmp/bmp", filename), arcname=os.path.join("content/data", filename))
for filename in os.listdir("additional_files/translation/bmp"):
    zipObj.write(os.path.join("additional_files/translation/bmp", filename), arcname=os.path.join("content/data", filename))

for filename in os.listdir("_tmp/def"):
    zipObj.write(os.path.join("_tmp/def", filename), arcname=os.path.join("content/sprites", filename))

for filename in os.listdir("additional_files/translation/txt"):
    zipObj.write(os.path.join("additional_files/translation/txt", filename), arcname=os.path.join("content/data", filename))

for filename in os.listdir("additional_files/translation/campaign"):
    if filename != "extra":
        zipObj.write(os.path.join("additional_files/translation/campaign", filename), arcname=os.path.join("content/data", filename))

if os.environ["APPEND_SOUND"] == "1":
    for filename in os.listdir("_tmp/snd"):
        zipObj.write(os.path.join("_tmp/snd", filename), arcname=os.path.join("content/sounds", filename))

if os.environ["APPEND_VIDEO"] == "1":
    for filename in os.listdir("_tmp/vid"):
        zipObj.write(os.path.join("_tmp/vid", filename), arcname=os.path.join("content/video", filename))

zipObj.close()