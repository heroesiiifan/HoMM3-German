#Braucht dekomprimiertes gzip

import sys
import re
import os
import copy

mode = "BOTH"

if mode == "READ" or mode == "BOTH":
    for filename in sorted(os.listdir("_tmp/hota_camp")):
        if filename.lower().startswith("raw_") and not filename.lower().endswith("txt"):
            f = open("_tmp/hota_camp/" + filename, 'rb')
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
                    #string_new += ret_str.group(0).decode(encoding='cp1252') + "\r\n===========================\r\n"
                    string_new += file_content[ret_str.start(0):ret_str.start(0)+len_].decode(encoding='cp1252') + "\r\n===========================\r\n"
            string_new = string_new[:-len("\r\n===========================\r\n")]
            with open("_tmp/hota_camp/" + filename + ".txt", 'wb') as the_file:
                the_file.write(str.encode(string_new, encoding='cp1252'))



if mode == "WRITE" or mode == "BOTH":
    for filename in sorted(os.listdir("_tmp/hota_camp")):
        if filename.lower().startswith("raw_") and not filename.lower().endswith("txt"):
            f = open("_tmp/hota_camp/" + filename, 'rb')
            file_content = f.read()
            f.close()

            with open("_tmp/hota_camp/" + filename + ".txt", 'rb') as the_file:
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
            
            f = open("_tmp/hota_camp/" + filename, 'wb')
            f.write(file_content)
            f.close()
pass