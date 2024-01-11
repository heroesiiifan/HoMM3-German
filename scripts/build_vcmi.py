#!/usr/bin/env python3

from zipfile import ZipFile
import zipfile
import os
from os.path import basename
import pathlib
import shutil

zipObj = ZipFile('_out/HoMM3DE_VCMI_veraltet.zip', 'w', zipfile.ZIP_STORED)

zipObj.write(os.path.join("additional_files/vcmi", "mod.json"), arcname=os.path.join("", "mod.json"))

for filename in os.listdir("additional_files/vcmi/config"):
    zipObj.write(os.path.join("additional_files/vcmi/config", filename), arcname=os.path.join("content/config", filename))

if os.environ["DEEPL_TRANSLATION"]:
    for filename in os.listdir("additional_files/translation/deepl/maps/out"):
        if not filename.startswith("[") and filename not in os.listdir("homm3_files/RoE_de/Maindisk/Maps") and filename not in os.listdir("homm3_files/SoD_de/Installation/Maps"): zipObj.write(os.path.join("additional_files/translation/deepl/maps/out", filename), arcname=os.path.join("content/maps", filename))
for filename in os.listdir("homm3_files/RoE_de/Maindisk/Maps"):
    zipObj.write(os.path.join("homm3_files/RoE_de/Maindisk/Maps", filename), arcname=os.path.join("content/maps", filename))
for filename in os.listdir("homm3_files/SoD_de/Installation/Maps"):
    if filename not in os.listdir("homm3_files/RoE_de/Maindisk/Maps"): zipObj.write(os.path.join("homm3_files/SoD_de/Installation/Maps", filename), arcname=os.path.join("content/maps", filename))
for filename in os.listdir("additional_files/translation/campaign/extra"):
    zipObj.write(os.path.join("additional_files/translation/campaign/extra", filename), arcname=os.path.join("content/maps", filename))
for filename in os.listdir("additional_files/translation/campaign/chronicles"):
    zipObj.write(os.path.join("additional_files/translation/campaign/chronicles", filename), arcname=os.path.join("content/maps", filename))

for filename in os.listdir("_tmp/fnt"):
    zipObj.write(os.path.join("_tmp/fnt", filename), arcname=os.path.join("content/data", filename))

for filename in os.listdir("_tmp/bmp"):
    zipObj.write(os.path.join("_tmp/bmp", filename), arcname=os.path.join("content/data", filename))
for filename in os.listdir("additional_files/translation/bmp"):
    zipObj.write(os.path.join("additional_files/translation/bmp", filename), arcname=os.path.join("content/data", filename))

for filename in os.listdir("_tmp/def"):
    zipObj.write(os.path.join("_tmp/def", filename), arcname=os.path.join("content/sprites", filename))
for filename in os.listdir("additional_files/translation/def"):
    zipObj.write(os.path.join("additional_files/translation/def", filename), arcname=os.path.join("content/sprites", filename))

for filename in os.listdir("additional_files/translation/txt"):
    zipObj.write(os.path.join("additional_files/translation/txt", filename), arcname=os.path.join("content/data", filename))

for filename in os.listdir("additional_files/translation/campaign"):
    if filename != "extra" and filename != "chronicles" and filename not in os.listdir("_tmp/camp"):
        zipObj.write(os.path.join("additional_files/translation/campaign", filename), arcname=os.path.join("content/data", filename))
for filename in os.listdir("_tmp/camp"):
    zipObj.write(os.path.join("_tmp/camp", filename), arcname=os.path.join("content/data", filename)) 

if os.environ["APPEND_SOUND"] == "1":
    for filename in os.listdir("_tmp/snd"):
        zipObj.write(os.path.join("_tmp/snd", filename), arcname=os.path.join("content/sounds", filename))

if os.environ["APPEND_VIDEO"] == "1":
    for filename in os.listdir("_tmp/vid"):
        zipObj.write(os.path.join("_tmp/vid", filename), arcname=os.path.join("content/video", filename))

zipObj.close()

#Addon Chronicles
if not os.path.exists("_tmp/vcmi_chronicles"): os.makedirs("_tmp/vcmi_chronicles")
with zipfile.ZipFile("homm3_files/vcmi/heroesChronicles_v1.0.zip", 'r') as zip_ref:
    zip_ref.extractall("_tmp/vcmi_chronicles")

shutil.copy("additional_files/translation/campaign/chronicles/Warlords of the Wasteland.h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/01warlordsOfTheWasteland/content/maps/Warlords of the Wasteland.h3c")
shutil.copy("additional_files/translation/campaign/chronicles/Conquest of the Underworld.h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/02conquestOfTheUnderworld/content/maps/Conquest of the Underworld.h3c")
shutil.copy("additional_files/translation/campaign/chronicles/Masters of the Elements.h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/03mastersOfTheElements/content/maps/Masters of the Elements.h3c")
shutil.copy("additional_files/translation/campaign/chronicles/Clash of the Dragons.h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/04clashOfTheDragons/content/maps/Clash of the Dragons.h3c")
shutil.copy("additional_files/translation/campaign/extra/WorldTree(dt).h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/05theWorldTree/content/maps/World Tree.h3c")
shutil.copy("additional_files/translation/campaign/extra/FieryMoon(dt).h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/06theFieryMoon/content/maps/The Fiery Moon.h3c")
shutil.copy("additional_files/translation/campaign/chronicles/Revolt of the Beastmasters.h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/07revoltOftheBeastmaster/content/maps/Revolt of the Beastmasters.h3c")
shutil.copy("additional_files/translation/campaign/chronicles/The Sword of Frost.h3c", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/08theSwordOfFrost/content/maps/The Sword of Frost.h3c")

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

copy_and_overwrite("_tmp/chronicles/01_snd/", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/01warlordsOfTheWasteland/content/sounds/")
copy_and_overwrite("_tmp/chronicles/02_snd/", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/02conquestOfTheUnderworld/content/sounds/")
copy_and_overwrite("_tmp/chronicles/03_snd/", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/03mastersOfTheElements/content/sounds/")
copy_and_overwrite("_tmp/chronicles/04_snd/", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/04clashOfTheDragons/content/sounds/")
copy_and_overwrite("_tmp/chronicles/0708_snd/", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/07revoltOftheBeastmaster/content/sounds/")
copy_and_overwrite("_tmp/chronicles/0708_snd/", "_tmp/vcmi_chronicles/heroesChronicles_v1.0/heroesChronicles/mods/08theSwordOfFrost/content/sounds/")

shutil.make_archive("_out/HoMM3DE_VCMI_heroesChronicles_de_v1.0_veraltet", 'zip', "_tmp/vcmi_chronicles")