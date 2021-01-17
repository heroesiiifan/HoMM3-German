#!/usr/bin/env python3

import clr
import os
import os.path
from System.Reflection import Assembly
from System.Reflection import BindingFlags
import System
from System.Text import Encoding
from System import Type

hota = Assembly.LoadFile(os.getcwd() + "/tools/HotA editor.exe")
hdat = hota.GetType("HotA_editor.Hdat")

hdata = System.Activator.CreateInstance(hdat)
t = hdata.GetType()
mi = t.GetMethod("ReadFile", BindingFlags.Instance | BindingFlags.NonPublic)
r = mi.Invoke(hdata, ["homm3_files/HotA/HotA.dat", Encoding.GetEncoding("windows-1250")])

for item in r.Items:
    if not os.path.exists("_tmp/HotA_txt/" + item.Name): os.makedirs("_tmp/HotA_txt/" + item.Name)
    if item.Data1 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data1.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data1, encoding='cp1250'))
    if item.Data2 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data2.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data2, encoding='cp1250'))
    if item.Data3 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data3.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data3, encoding='cp1250'))
    if item.Data4 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data4.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data4, encoding='cp1250'))
    if item.Data5 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data5.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data5, encoding='cp1250'))
    if item.Data6 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data6.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data6, encoding='cp1250'))
    if item.Data7 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data7.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data7, encoding='cp1250'))
    if item.Data8 != "":
        with open(os.path.join("_tmp/HotA_txt/" + item.Name, "data8.txt"), 'w+b') as the_file:
            the_file.write(str.encode(item.Data8, encoding='cp1250'))

file_path = '_tmp/HotA_txt' #debug zum checken ob Ergebnis-Dat identisch
file_path = 'additional_files/hota/dat_translation'

for path, directories, files in os.walk(file_path):
    for file in files:
        #print('found %s' % os.path.join(path, file))
        internal_path = path.replace(file_path, "")[1:]

        for item in r.Items:
            if item.Name == internal_path:
                with open(os.path.join(path, file), "r+b") as f:
                    text = f.read()
                    text = text.decode(encoding='cp1250')

                    if file.startswith("data1"): item.Data1 = text
                    if file.startswith("data2"): item.Data2 = text
                    if file.startswith("data3"): item.Data3 = text
                    if file.startswith("data4"): item.Data4 = text
                    if file.startswith("data5"): item.Data5 = text
                    if file.startswith("data6"): item.Data6 = text
                    if file.startswith("data7"): item.Data7 = text
                    if file.startswith("data8"): item.Data8 = text

if not os.path.exists("_tmp/HotA_patched"): os.makedirs("_tmp/HotA_patched")
mi = t.GetMethod("WriteFile", BindingFlags.Instance | BindingFlags.NonPublic)
mi.Invoke(hdata, ["_tmp/HotA_patched/" + "HotA.dat", r, Encoding.GetEncoding("windows-1250")])