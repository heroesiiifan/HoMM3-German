import subprocess
import os
import gzip
import zlib
import glob
import re
import shutil

if not os.path.exists("_tmp/hota_camp"): os.makedirs("_tmp/hota_camp")

if not os.path.exists("_tmp/hota_camp/1_splitted"): os.makedirs("_tmp/hota_camp/1_splitted")
if not os.path.exists("_tmp/hota_camp/2_unzipped"): os.makedirs("_tmp/hota_camp/2_unzipped")
if not os.path.exists("_tmp/hota_camp/3_extracted_strings"): os.makedirs("_tmp/hota_camp/3_extracted_strings")
if not os.path.exists("_tmp/hota_camp/4_modified_strings"): os.makedirs("_tmp/hota_camp/4_modified_strings")
if not os.path.exists("_tmp/hota_camp/5_unzipped"): os.makedirs("_tmp/hota_camp/5_unzipped")
if not os.path.exists("_tmp/hota_camp/6_splitted"): os.makedirs("_tmp/hota_camp/6_splitted")
if not os.path.exists("_tmp/hota_camp/7_out"): os.makedirs("_tmp/hota_camp/7_out")

#Zweimal ausführen und vorm zweiten mal /4 befüllen

#Get Campaign
output = subprocess.Popen(["tools/mmarch.exe", "extract", "homm3_files/HotA/Data/HotA_lng.lod", "_tmp/hota_camp", "*.h3c"], stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

#Step 1 Split
for filename in os.listdir("_tmp/hota_camp"):
    if filename.lower().endswith(".h3c"):
        subprocess.Popen(["tools/splitter.exe", "_tmp/hota_camp/" + filename], stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
        for filename in sorted(os.listdir("_tmp/hota_camp")):
            if filename.lower().endswith((".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11", ".12", ".13", ".14", ".15")):
                shutil.move("_tmp/hota_camp/" + filename, "_tmp/hota_camp/1_splitted/" + filename)

#Step2 UNZIP
for filename in sorted(os.listdir("_tmp/hota_camp/1_splitted")):
    f = gzip.open("_tmp/hota_camp/1_splitted/" + filename, 'rb')
    file_content = f.read()
    f.close()
    f = open("_tmp/hota_camp/2_unzipped/" + filename, 'wb')
    f.write(file_content)
    f.close()

#Step3 Extract
for filename in sorted(os.listdir("_tmp/hota_camp/2_unzipped")):
    f = open("_tmp/hota_camp/2_unzipped/" + filename, 'rb')
    file_content = f.read()
    f.close()

    chars = b"A-Za-z0-9/\-:.,;_$%'()[\]<>\?\! \x93\x94"
    shortest_run = 4

    regexp = b'[%s]{%d,}' % (chars, shortest_run)
    pattern = re.compile(regexp)

    string_new = ""
    for ret_str in list(pattern.finditer(file_content)):
        print(ret_str.group(0))
        tmp = file_content[ret_str.start(0)-4:ret_str.start(0)]
        len_ = tmp[1] << 8 | tmp[0]
        if tmp[2] == 0 and tmp[3] == 0:
            string_new += file_content[ret_str.start(0):ret_str.start(0)+len_].decode(encoding='cp1252') + "\r\n===========================\r\n"
    string_new = string_new[:-len("\r\n===========================\r\n")]
    with open("_tmp/hota_camp/3_extracted_strings/" + filename + ".txt", 'wb') as the_file:
        the_file.write(str.encode(string_new, encoding='cp1252'))

#Step4 Replace
for filename in sorted(os.listdir("_tmp/hota_camp/2_unzipped")):
    f = open("_tmp/hota_camp/2_unzipped/" + filename, 'rb')
    file_content = f.read()
    f.close()

    with open("_tmp/hota_camp/4_modified_strings/" + filename + ".txt", 'rb') as the_file:
        strings = the_file.read().decode(encoding='cp1252').split("\r\n===========================\r\n")
        strings.reverse()
        strings = [e.replace("\r\n", "\n") for e in strings]

    chars = b"A-Za-z0-9/\-:.,;_$%'()[\]<>\?\! \x93\x94"
    shortest_run = 4

    regexp = b'[%s]{%d,}' % (chars, shortest_run)
    pattern = re.compile(regexp)

    lst = list(pattern.finditer(file_content))
    lst.reverse()
    i = 0
    for ret_str in lst:
        print(ret_str.group(0))
        tmp = file_content[ret_str.start(0)-4:ret_str.start(0)]
        len_ = tmp[1] << 8 | tmp[0]
        if tmp[2] == 0 and tmp[3] == 0:
            str_ = str.encode(strings[i], encoding='cp1252')
            tmp = bytes([0xff & len(str_)]) + bytes([(0xff00 & len(str_)) >> 8]) + b'\x00\x00'
            file_content = file_content[0:ret_str.start(0)-4] + tmp + str_ + file_content[ret_str.start(0)+len_:]

            i += 1
    
    f = open("_tmp/hota_camp/5_unzipped/" + filename, 'wb')
    f.write(file_content)
    f.close()

#Step5 ZIP
for filename in sorted(os.listdir("_tmp/hota_camp/5_unzipped")):
    f = open("_tmp/hota_camp/5_unzipped/" + filename, 'rb')
    file_content = f.read()
    f.close()
    f = open("_tmp/hota_camp/6_splitted/" + filename, 'wb')
    co = zlib.compressobj(wbits=31)
    f.write(co.compress(file_content) + co.flush())
    f.close()

#Step5b Filesizes
for filename in sorted(os.listdir("_tmp/hota_camp/5_unzipped")):
    if filename.endswith("1"):
        f = open("_tmp/hota_camp/5_unzipped/" + filename, 'rb')
        file_content = f.read()
        f.close()

        regexp = b'\.h3m'
        pattern = re.compile(regexp)
        lst = list(pattern.finditer(file_content))
        i = 2
        for ret_str in lst:
            size = os.path.getsize("_tmp/hota_camp/6_splitted/" + filename[:-1] + str(i))
            tmp = bytes([0xff & size]) + bytes([(0xff00 & size) >> 8])

            pos = ret_str.start(0)
            file_content = file_content[0:pos+4] + tmp + file_content[pos+4+2:]

            i += 1

        f = open("_tmp/hota_camp/5_unzipped/" + filename, 'wb')
        f.write(file_content)
        f.close()


#Step5 ZIP
for filename in sorted(os.listdir("_tmp/hota_camp/5_unzipped")):
    f = open("_tmp/hota_camp/5_unzipped/" + filename, 'rb')
    file_content = f.read()
    f.close()
    f = open("_tmp/hota_camp/6_splitted/" + filename, 'wb')
    co = zlib.compressobj(wbits=31)
    f.write(co.compress(file_content) + co.flush())
    f.close()

#Step6 Combine
for filegroup in glob.glob("_tmp/hota_camp/*.h3c"):
    comb = ""
    for filename in sorted(os.listdir("_tmp/hota_camp/6_splitted")):
        groupname = os.path.basename(filegroup)
        
        if filename.lower().endswith((".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", ".10", ".11", ".12", ".13", ".14", ".15")) and filename.startswith(groupname):
            comb += "\"" + os.path.abspath("_tmp/hota_camp/6_splitted/" + filename) + "\"+"
            print("_tmp/hota_camp/6_splitted/" + filename)
    comb = comb[:-1]
    os.system("copy" + " /b " + comb + " \"" + os.path.abspath("_tmp/hota_camp/7_out/" + groupname) + "\"")


pass