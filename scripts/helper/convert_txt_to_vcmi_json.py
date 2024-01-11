#Aktuell nur Test - bessere Variante: nutze VCMI für die Konverierung installiere Mod, dann: "vcmiclient.exe > a.txt" und dann eingabe von "convert txt", Ende, File zu json ausarbeiten.

import os
import json
import re

from sqlalchemy import false

translation = {}

path = r"h3_/additional_files/translation/txt"
for filename in os.listdir(path): #anpassen
    with open(os.path.join(path, filename), "r+b") as f:
        text = f.read()
        text = text.decode(encoding='cp1252')
 
        string_new = ""

        inside_quote = False
        i = 0
        for c in text:
            if c == "\"":
                inside_quote = not inside_quote
                string_new += c
            elif c == "\n":
                if not inside_quote:
                    tmp = re.sub(r'(^|[^\"])(\"{1})([^\"]|$)', r'\1\3', string_new)
                    tmp = re.sub(r'(^|[^\"])(\"{2})([^\"]|$)', r'\1"\3', tmp)
                    tmp = re.sub(r'(^|[^\"])(\"{3})([^\"]|$)', r'\1"\3', tmp)
                    translation['core.' + filename.lower().split('.')[0] + '.' + str(i)] = tmp
                    i += 1
                    string_new = ""
                else:
                    string_new += c
            elif c == "\r":
                pass
            else:
                string_new += c

json_object = json.dumps(translation, indent=4, ensure_ascii=False)
with open(r"translation.json", "w", encoding='cp1252') as outfile:
    outfile.write(json_object)

pass