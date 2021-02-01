import subprocess
import os
import io
import pathlib
import shutil
import glob

#ATTENTION- THis Workflow doesn't work as aspected...

if not os.path.exists("_tmp/hota_camp"): os.makedirs("_tmp/hota_camp")
output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/HotA/Data/HotA_lng.lod", "_tmp/hota_camp", "*.h3c"], stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

shutil.copyfile("tools/splitter.exe", "_tmp/hota_camp/splitter.exe")

for filename in os.listdir("_tmp/hota_camp"):
    if filename.lower().endswith(".h3c"):
        print("_tmp/hota_camp/" + filename)
        output = subprocess.Popen(["_tmp/hota_camp/splitter.exe", "_tmp/hota_camp/" + filename], stdout=subprocess.PIPE).communicate()[0].decode('cp1252')


# HIER HALTEPUNKT und Dateien modifizieren!!!
pass

# 2-n im normalen Mapeditor
# Namen müssen passen?

# .1 - Also Kampagnen mit Hex-Editor bearbeiten 
# Stringlänge anpassen
# Format für Stringlänge:       [LOW_BYTE] [HIGH_BYTE] 00 00 {STRING...}


for filegroup in glob.glob("_tmp/hota_camp/*.h3c"):
    comb = ""
    for filename in sorted(os.listdir("_tmp/hota_camp")):
        groupname = os.path.basename(filegroup)
        
        if filename.lower().endswith((".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11", ".12", ".13", ".14", ".15")) and filename.startswith(groupname):
            comb += "\"" + os.path.abspath("_tmp/hota_camp/" + filename) + "\"+"
            print("_tmp/hota_camp/" + filename)
    comb = comb[:-1]
    os.system("copy" + " /b " + comb + " \"" + os.path.abspath("_tmp/hota_camp/" + groupname + ".new") + "\"")
