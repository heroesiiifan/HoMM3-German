#!/usr/bin/env python3

import os
from os.path import basename
import pathlib
import subprocess
from shutil import copyfile

if not os.path.exists("_tmp/fnt"): os.makedirs("_tmp/fnt")
output = subprocess.Popen(["tools/mmarch.exe", "list", "homm3_files/RoE_de/Maindisk/Data/H3bitmap.lod", """|"""], stdout=subprocess.PIPE).communicate()[0].decode('cp1252').split("|")
fnt = list(filter(lambda x: x.lower().endswith(".fnt"), output))
output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/RoE_de/Maindisk/Data/H3bitmap.lod", "_tmp/fnt"] + fnt, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

if not os.path.exists("_tmp/bmp"): os.makedirs("_tmp/bmp")
output = subprocess.Popen(["tools/mmarch.exe", "list", "homm3_files/RoE_de/Maindisk/Data/H3bitmap.lod", """|"""], stdout=subprocess.PIPE).communicate()[0].decode('cp1252').split("|")
bmp = list(filter(lambda x: x.lower() in ["advopts.pcx", "altarmon.pcx", "campback.pcx", "questlog.pcx", "tpmrkabs.pcx", "tpmrkass.pcx", "tpmrkcrs.pcx", "tpmrkpts.pcx", "tpmrkres.pcx"], output))
output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/RoE_de/Maindisk/Data/H3bitmap.lod", "_tmp/bmp"] + bmp, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

if not os.path.exists("_tmp/def"): os.makedirs("_tmp/def")
output = subprocess.Popen(["tools/mmarch.exe", "list", "homm3_files/RoE_de/Maindisk/Data/h3sprite.lod", """|"""], stdout=subprocess.PIPE).communicate()[0].decode('cp1252').split("|")
def_ = list(filter(lambda x: x.lower() in ["cbbegib.def", "cbcancb.def", "cbrestb.def", "hisccam.def", "hiscres.def", "hiscsta.def", "hiscext.def", "mubjoin.def", "scbutt3.def", "scnrback.def", "scnrlod.def", "scnrsav.def", "soload.def", "somain.def", "soquit.def", "soretrn.def", "sorstrt.def", "sosave.def", "scnrbeg.def", "cmpscan.def", "codefaul.def", "icm011.def", "icm012.def", "trrecb.def"], output))
output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/RoE_de/Maindisk/Data/h3sprite.lod", "_tmp/def"] + def_, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

if not os.path.exists("_tmp/def"): os.makedirs("_tmp/def")
output = subprocess.Popen(["tools/mmarch.exe", "list", "homm3_files/Chronicles_de/_common/lsprite.lod", """|"""], stdout=subprocess.PIPE).communicate()[0].decode('cp1252').split("|")
def_ = list(filter(lambda x: x.lower() in ["camcusl.def", "sysob12.def", "sysob13.def", "scnrexi.def", "gspexit.def", "gspbgin.def", "camprst.def", "campld.def", "campcn.def", "avrcgen0.def", "avrcgen1.def", "avrcgen2.def", "avrcgen3.def", "avrcgen4.def", "avrcgen5.def", "avrcgen6.def", "avrcgen7.def", "avrcgn00.def", "avrcgn01.def", "avrcgn02.def", "avrcgn03.def", "avrcgn04.def", "avrcgn05.def", "avrcgn06.def", "avrcgn07.def", "avrcgn08.def", "avwmon1.def", "avwmon2.def", "avwmon3.def", "avwmon4.def", "avwmon5.def", "avwmon6.def", "avwmon7.def", "avwmrnd0.def", "avzevnt0.def", "avzgrail.def"], output))
output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/Chronicles_de/_common/lsprite.lod", "_tmp/def"] + def_, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

if os.environ["APPEND_SOUND"] == "1":
    if not os.path.exists("_tmp/snd"): os.makedirs("_tmp/snd")
    output = subprocess.Popen(["tools/mmarch.exe", "list", "homm3_files/RoE_de/Datadisk/heroes3.snd", """|"""], stdout=subprocess.PIPE).communicate()[0].decode('cp1252').split("|")
    snd = list(filter(lambda x: True, output))
    output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/RoE_de/Datadisk/heroes3.snd", "_tmp/snd"] + snd, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

if os.environ["APPEND_VIDEO"] == "1":
    if not os.path.exists("_tmp/vid"): os.makedirs("_tmp/vid")
    output = subprocess.Popen(["tools/mmarch.exe", "list", "homm3_files/RoE_de/Datadisk/heroes3.vid", """|"""], stdout=subprocess.PIPE).communicate()[0].decode('cp1252').split("|")
    vid = list(filter(lambda x: x.lower() in ["endgame.smk", "h3intro.smk"], output))
    output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/RoE_de/Datadisk/heroes3.vid", "_tmp/vid"] + vid, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
