#!/usr/bin/env python3

from zipfile import ZipFile
import zipfile
import os
from os.path import basename
import pathlib

def correct_line_ending(file_in, file_out):
    with open(file_in, "r+b") as f:
        text = f.read()
        text = text.decode(encoding='cp1252')
        string_new = ""

        inside_quote = False
        for c in text:
            if c == "\"":
                inside_quote = not inside_quote
                string_new += c
            elif c == "\r":
                if not inside_quote: string_new += c
            else:
                string_new += c
            char_last = c

        with open(file_out, 'w+b') as the_file:
            the_file.write(str.encode(string_new, encoding='cp1252'))


zipObj = ZipFile('_out/HoMM3DE_HD.zip', 'w', zipfile.ZIP_STORED)

zipObj.write(os.path.join("additional_files/hd", "#de.ini"), arcname=os.path.join("Lang", "#de.ini"))
zipObj.write(os.path.join("additional_files/hd", "Pack.ini"), arcname=os.path.join("Packs/German", "Pack.ini"))

zipObj.write(os.path.join("_tmp/fnt/", "MedFont.fnt"), arcname=os.path.join("Common", "cham.fnt"))
zipObj.write(os.path.join("additional_files/hd/def/", "icm011qe.def"), arcname=os.path.join("Lang/#de", "icm011qe.def"))
zipObj.write(os.path.join("additional_files/hd/def/", "icm012qe.def"), arcname=os.path.join("Lang/#de", "icm012qe.def"))
zipObj.write(os.path.join("additional_files/hd/def/", "Files.ini"), arcname=os.path.join("Lang/#de", "Files.ini"))

if os.environ["DEEPL_TRANSLATION"] == "1":
    for filename in os.listdir("additional_files/translation/deepl/maps/out"):
        if not filename.startswith("[") and filename not in os.listdir("homm3_files/RoE_de/Maindisk/Maps") and filename not in os.listdir("homm3_files/SoD_de/Installation/Maps"): zipObj.write(os.path.join("additional_files/translation/deepl/maps/out", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("homm3_files/RoE_de/Maindisk/Maps"):
    zipObj.write(os.path.join("homm3_files/RoE_de/Maindisk/Maps", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("homm3_files/SoD_de/Installation/Maps"):
    if filename not in os.listdir("homm3_files/RoE_de/Maindisk/Maps"): zipObj.write(os.path.join("homm3_files/SoD_de/Installation/Maps", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("additional_files/translation/campaign/extra"):
    zipObj.write(os.path.join("additional_files/translation/campaign/extra", filename), arcname=os.path.join("_Custom_Campaign", filename))
for filename in os.listdir("additional_files/translation/campaign/chronicles"):
    zipObj.write(os.path.join("additional_files/translation/campaign/chronicles", filename), arcname=os.path.join("_Custom_Campaign", filename))

for filename in os.listdir("_tmp/fnt"):
    zipObj.write(os.path.join("_tmp/fnt", filename), arcname=os.path.join("Packs/German", filename))

for filename in os.listdir("additional_files/hd/bmp/"):
    zipObj.write(os.path.join("additional_files/hd/bmp/", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("_tmp/bmp"):
    zipObj.write(os.path.join("_tmp/bmp", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("additional_files/translation/bmp"):
    if filename not in os.listdir("additional_files/hd/bmp/"):
        zipObj.write(os.path.join("additional_files/translation/bmp", filename), arcname=os.path.join("Packs/German", filename))

for filename in os.listdir("_tmp/def"):
    zipObj.write(os.path.join("_tmp/def", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("additional_files/translation/def"):
    zipObj.write(os.path.join("additional_files/translation/def", filename), arcname=os.path.join("Packs/German", filename))
  
for filename in os.listdir("additional_files/translation/audio"):
    zipObj.write(os.path.join("additional_files/translation/audio", filename), arcname=os.path.join("Packs/German", filename))

for filename in os.listdir("additional_files/translation/txt"):
    correct_line_ending(os.path.join("additional_files/translation/txt", filename), os.path.join("_tmp", "file.tmp"))
    zipObj.write(os.path.join("_tmp", "file.tmp"), arcname=os.path.join("Packs/German", filename))

for filename in os.listdir("additional_files/translation/campaign"):
    if "extra" not in filename and "chronicles" not in filename and filename not in os.listdir("_tmp/camp"):
        zipObj.write(os.path.join("additional_files/translation/campaign", filename), arcname=os.path.join("Packs/German", filename))
for filename in os.listdir("_tmp/camp"):
    zipObj.write(os.path.join("_tmp/camp", filename), arcname=os.path.join("Packs/German", filename))

if os.environ["APPEND_SOUND"] == "1":
    for filename in os.listdir("_tmp/snd"):
        zipObj.write(os.path.join("_tmp/snd", filename), arcname=os.path.join("Packs/German", filename[:-4]))

if os.environ["APPEND_VIDEO"] == "1":
    for filename in os.listdir("_tmp/vid"):
        zipObj.write(os.path.join("_tmp/vid", filename), arcname=os.path.join("Packs/German", filename))

zipObj.close()