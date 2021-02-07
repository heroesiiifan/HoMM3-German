import subprocess
import os
import io
import pathlib
import shutil
import glob
import gzip
import zlib

mode = "READ"

if mode == "READ":
    shutil.rmtree("_tmp/hota_camp")
    if not os.path.exists("_tmp/hota_camp"): os.makedirs("_tmp/hota_camp")
    output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/HotA/Data/HotA_lng.lod", "_tmp/hota_camp", "*.h3c"], stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

    shutil.copyfile("tools/splitter.exe", "_tmp/hota_camp/splitter.exe")

    for filename in os.listdir("_tmp/hota_camp"):
        if filename.lower().endswith(".h3c"):
            print("_tmp/hota_camp/" + filename)
            output = subprocess.Popen(["_tmp/hota_camp/splitter.exe", "_tmp/hota_camp/" + filename], stdout=subprocess.PIPE).communicate()[0].decode('cp1252')


    for filename in sorted(os.listdir("_tmp/hota_camp")):
        if filename.lower().endswith((".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11", ".12", ".13", ".14", ".15")) and filename.lower().startswith("h"):
            f = gzip.open("_tmp/hota_camp/" + filename, 'rb')
            file_content = f.read()
            f.close()
            f = open("_tmp/hota_camp/" + "raw_" + filename, 'wb')
            f.write(file_content)
            f.close()






# mit h3m_string_editor.py bearbeiten 
# Stringlänge anpassen
# Format für Stringlänge:       [LOW_BYTE] [HIGH_BYTE] 00 00 {STRING...}

if mode == "WRITE":
    for filename in sorted(os.listdir("_tmp/hota_camp")):
        if filename.lower().startswith("raw_"):
            f = open("_tmp/hota_camp/" + filename, 'rb')
            file_content = f.read()
            f.close()
            f = open("_tmp/hota_camp/" + "rezipped_" + filename, 'wb')
            #gz = gzip.GzipFile('', 'wb', 9, f, 0.)
            #gz.write(file_content)
            #gz.close()
            co = zlib.compressobj(wbits=31)
            f.write(co.compress(file_content) + co.flush())
            f.close()



    for filegroup in glob.glob("_tmp/hota_camp/*.h3c"):
        comb = ""
        for filename in sorted(os.listdir("_tmp/hota_camp")):
            groupname = os.path.basename(filegroup)
            
            if filename.lower().endswith((".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11", ".12", ".13", ".14", ".15")) and filename.startswith("rezipped_raw_" + groupname):
                comb += "\"" + os.path.abspath("_tmp/hota_camp/" + filename) + "\"+"
                print("_tmp/hota_camp/" + filename)
        comb = comb[:-1]
        if not os.path.exists("_tmp/hota_camp/out"): os.makedirs("_tmp/hota_camp/out")
        os.system("copy" + " /b " + comb + " \"" + os.path.abspath("_tmp/hota_camp/out/" + groupname) + "\"")