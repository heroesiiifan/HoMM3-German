#!/usr/bin/env python3

from zipfile import ZipFile
import zipfile
import os
from os.path import basename
import sys
import pathlib
import subprocess
import shutil

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "scripts/requirements.txt"])

os.chdir(pathlib.Path(__file__).parent.parent.absolute())

os.environ["APPEND_VIDEO"] = "1"
os.environ["APPEND_SOUND"] = "1"

os.environ["DEEPL_TRANSLATION"] = "1"

#Ordner löschen
if os.path.exists("_out"): shutil.rmtree("_out")
if os.path.exists("_tmp"): shutil.rmtree("_tmp")

#Ordner erstellen
if not os.path.exists("_out"): os.makedirs("_out")
if not os.path.exists("_tmp"): os.makedirs("_tmp")

#Dateien auflisten
folder = "homm3_files"
with open("homm3_files/benoetigt.txt", "w") as f:
    for foldername, subfolders, filenames in os.walk(folder):
        if foldername == folder:
            archive_folder_name = ''
        else:
            archive_folder_name = os.path.relpath(foldername, folder)
        for filename in filenames:
            if filename != "benoetigt.txt":
                f.write(os.path.join(archive_folder_name, filename) + "\n")

#Source sammeln
exec(open("scripts/build_public_source.py").read())

#Dateien extrahieren
exec(open("scripts/extract_files.py").read())

#VCMI erstellen
exec(open("scripts/build_vcmi.py").read())

#HD erstellen
exec(open("scripts/build_hd.py").read())

#HotA erstellen
exec(open("scripts/pack_hdat.py").read())
exec(open("scripts/build_hota.py").read())

#Alle zusammen zippen
files = []
files.append("README.md")
files.append("CREDITS.md")
for filename in os.listdir("_out"):
    if not filename.startswith("HoMM3DE_RELEASE.7z"):
        files.append(os.path.join("_out", filename))

output = subprocess.Popen(["7z", "a", "-t7z", "_out\\HoMM3DE_RELEASE.7z"] + files + ["-m0=LZMA:d1024m:fb273", "-mx=7"], stdout=subprocess.PIPE).communicate()[0]