#!/usr/bin/env python3

# Dateien mit Winmerge verglichen
# Complete <-> HotA
# Am besten 2x Winmerge öffnen 1. DE_alt <-> DE_neu   2. EN_complete <-> EN_HotA
# Gleiche: übernommen
# Unterschiedliche: Versucht auf dt. zu übertragen und einen Patch mit Winmerge zu erstellen

from zipfile import ZipFile
import zipfile
from shutil import copyfile
import os
import whatthepatch
import subprocess

s = "additional_files/translation/txt/"
d = "_tmp/HotA_patched/txt/"

if not os.path.exists(d): os.makedirs(d)

identical = [ "Artslots.txt", "CampDiag.txt", "CastInfo.txt", "CmpEdCmd.txt", "CmpEditr.txt", "CrGen4.txt", "CrGenerc.txt", "Garrison.txt", "HallInfo.txt", "HeroScrn.txt", "JkText.txt", "Lcdesc.txt", "MineEvnt.txt", "OverView.txt", "PlColors.txt", "PriSkill.txt", "RandSign.txt", "Regions.txt", "ResTypes.txt", "SkillLev.txt", "TCommand.txt", "TentColr.txt", "TownName.txt", "TownType.txt", "TurnDur.txt", "TvrnInfo.txt", "VcDesc.txt", "Walls.txt" ]

for val in identical:
    copyfile(s + val, d + val)

for filename in os.listdir("additional_files/hota/txt"):
    if filename.endswith(".txt.diff"):
        filename_full = os.path.join("additional_files/hota/txt", filename)
        filename_raw = filename.replace(".txt.diff", "")
        with open(filename_full) as f:
            patch = f.read()
        with open(s + filename_raw + ".txt", "r+b") as f:
            src_content = f.read()
            src_content = src_content.decode(encoding='cp1252')
            original_name = os.path.basename(f.name)

        #patch
        diff = [x for x in whatthepatch.parse_patch(patch)]
        diff = diff[0]
        dst_content = whatthepatch.apply_diff(diff, src_content)
        dst_content = '\r\n'.join(dst_content)
        dst_content += '\r\n'

        #correct lineendings
        string_new = ""
        inside_quote = False
        for c in dst_content:
            if c == "\"":
                inside_quote = not inside_quote
                string_new += c
            elif c == "\r":
                if not inside_quote: string_new += c
            else:
                string_new += c
            char_last = c

        #save
        with open(os.path.join(d, original_name), 'w+b') as the_file:
            the_file.write(str.encode(string_new, encoding='cp1252'))


copyfile("homm3_files\HotA\Data\HotA.lod", "_tmp/HotA_patched/" + "HotA.lod")
copyfile("homm3_files\HotA\Data\HotA_lng.lod", "_tmp/HotA_patched/" + "HotA_lng.lod")

command = ["tools/mmarch.exe", "add", "_tmp/HotA_patched/" + "HotA.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/HotA_patched/" + "HotA_lng.lod"] + ["_tmp/HotA_patched/txt/" + s for s in os.listdir("_tmp/HotA_patched/txt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/HotA_patched/" + "HotA_lng.lod"] + ["_tmp/def/" + s for s in os.listdir("_tmp/def/")] + ["additional_files/hota/bmp/" + s for s in os.listdir("additional_files/hota/bmp/")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

zipObj = ZipFile('_out/HoMM3DE_HotA.zip', 'w', zipfile.ZIP_STORED)
zipObj.write(os.path.join("_tmp/HotA_patched/" + "HotA.lod"), arcname=os.path.join("", "HotA.lod"))
zipObj.write(os.path.join("_tmp/HotA_patched/" + "HotA_lng.lod"), arcname=os.path.join("", "HotA_lng.lod"))
zipObj.write(os.path.join("_tmp/HotA_patched/" + "HotA.dat"), arcname=os.path.join("", "HotA.dat"))
zipObj.close()