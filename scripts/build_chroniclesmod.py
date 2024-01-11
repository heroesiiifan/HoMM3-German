#!/usr/bin/env python3

from shutil import copyfile, copy
import os
import glob
import subprocess
from zipfile import ZipFile
import zipfile

def textadjustment(txt, camp):
    res = txt.replace("Armageddon's Blade-Kampagne auswählen", "Die Originalversion der Vorschauen.")
    res = res.replace("Restoration of Erathia-Kampagne auswählen", "Die Originalversion des Tutorials.")
    res = res.replace("Eigene Kampagne auswählen", "Wählen Sie Ihre eigene Chronik-Kampagne. Wenn Sie eine Kampagne erstellen, denken Sie an alle Porträts von Tarnum, die für eine bestimmte Chronik verwendet werden.")
    res = res.replace("Shadow of Death-Kampagne auswählen", "Die Originalversion der Kampagne.")

    tmp = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nLang lebe die Königin\tLang lebe die Königin\t\t\r\nBefreiung\tBefreiung\t\t\r\nKriegsbeute\tKriegsbeute\t\t\r\nLied für den Vater\tLied für den Vater\t\t\r\nDungeons und Teufel\tDungeons und Teufel\t\t\r\nLang lebe der König\tLang lebe der König\t\t\r\nSaat der Zwietracht\tSaat der Zwietracht\t\t\r\nDas Schwert Armageddon\tDas Schwert Armageddon\t\t\r\nDrachenblut\tDrachenblut\t\t\r\nDrachentöter\tDrachentöter\t\t\r\nFest des Lebens\tFest des Lebens\t\t\r\nTollkühner Starsinn\tTollkühner Starsinn\t\t\r\nMit Feuer spielen\tMit Feuer spielen\t\t\r\nHieb und Stich\tHieb und Stich\t\t\r\nGeburt eines Barbaren\tGeburt eines Barbaren\t\t\r\nNeuanfang\tNeuanfang\t\t\r\nElixier des Lebens\tElixier des Lebens\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nWeg des Totenbeschwörers\tWeg des Totenbeschwörers\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nUnheilige Allianz\tUnheilige Allianz\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nGespenst der Macht\tGespenst der Macht\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
    match camp:
        case 1:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. Revolt of the Beastmasters\tUpg. Revolt of the Beastmasters\t\r\nConquest of the Underworld\tConquest of the Underworld\r\nClash of the Dragons\tClash of the Dragons\t\r\nWarlords of the Wasteland\tWarlords of the Wasteland\r\n\r\nMasters of the Elements\tMasters of the Elements\r\n\r\n\r\nRevolt of the Beastmasters\tRevolt of the Beastmasters\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        case 2:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. The World Tree\tUpg. The World Tree\t\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nThe World Tree\tThe World Tree\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        case 3:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. The Sword of Frost\tUpg. The Sword of Frost\t\r\nConquest of the Underworld\tConquest of the Underworld\r\nClash of the Dragons\tClash of the Dragons\t\r\nWarlords of the Wasteland\tWarlords of the Wasteland\r\n\r\nMasters of the Elements\tMasters of the Elements\r\n\r\n\r\n\r\nThe Sword of Frost\tThe Sword of Frost\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        case 4:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. The Fiery Moon\tUpg. The Fiery Moon\t\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nThe Fiery Moon\tThe Fiery Moon\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        case 5:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. Conquest of the Underworld\tUpg. Conquest of the Underworld\t\r\nConquest of the Underworld\tConquest of the Underworld\r\nClash of the Dragons\tClash of the Dragons\t\r\nWarlords of the Wasteland\tWarlords of the Wasteland\r\n\r\nMasters of the Elements\tMasters of the Elements\r\n\r\n\r\nConquest of the Underworld\tConquest of the Underworld\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            res = res.replace("Einhörner\tKreaturenbonus: Einhörner\tErhöht Angriff und Verteidigung aller Einhörner oder Kriegseinhörner für jede erreichte Stufe nach der 6. Stufe.", "Schwertkämpfer\tKreaturenbonus: Schwertkämpfer\tErhöht Angriff und Verteidigung aller Schwertkämpfer oder Kreuzritter für jede erreichte Stufe nach der 4. Stufe.")
        case 6:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. Clash of the Dragons\tUpg. Clash of the Dragons\t\r\nConquest of the Underworld\tConquest of the Underworld\r\nClash of the Dragons\tClash of the Dragons\t\r\nWarlords of the Wasteland\tWarlords of the Wasteland\r\n\r\nMasters of the Elements\tMasters of the Elements\r\n\r\n\r\n\r\nClash of the Dragons\tClash of the Dragons\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        case 7:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. Masters of the Elements\tUpg. Masters of the Elements\t\r\nConquest of the Underworld\tConquest of the Underworld\r\nClash of the Dragons\tClash of the Dragons\t\r\nWarlords of the Wasteland\tWarlords of the Wasteland\r\n\r\nMasters of the Elements\tMasters of the Elements\r\n\r\n\r\nMasters of the Elements\tMasters of the Elements\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
        case 8:
            res = res.replace(tmp, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\nTutorial\tTutorial\t\t\r\n\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\t\r\n\t\r\nUpg. Warlords of the Wasteland\tUpg. Warlords of the Wasteland\t\r\nConquest of the Underworld\tConquest of the Underworld\r\nClash of the Dragons\tClash of the Dragons\t\r\nWarlords of the Wasteland\tWarlords of the Wasteland\r\n\r\nMasters of the Elements\tMasters of the Elements\r\n\r\n\r\nWarlords of the Wasteland\tWarlords of the Wasteland\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
            res = res.replace("Einhörner\tKreaturenbonus: Einhörner\tErhöht Angriff und Verteidigung aller Einhörner oder Kriegseinhörner für jede erreichte Stufe nach der 6. Stufe.", "Offensive\tSekundärer Fertigkeitsbonus: Offensive\tErhält einen Bonus von 5% pro Stufe auf den Prozentsatz der Offensiv-Fertigkeiten.")

    return res

def correct_line_ending_and_adjustments(file_in, file_out, camp):
    with open(file_in, "r+b") as f:
        text = f.read()
        text = text.decode(encoding='cp1252')
        text = textadjustment(text, camp)
        string_new = ""

        inside_quote = False
        for c in text:
            if c == "\"":
                inside_quote = not inside_quote
                string_new += c
            elif c == "\r":
                if not inside_quote: string_new += c
            else:
                string_new += c
            char_last = c

        with open(file_out, 'w+b') as the_file:
            the_file.write(str.encode(string_new, encoding='cp1252'))

def patch(fn1, fn2, camp):
    files = []
    for filename in os.listdir("additional_files/translation/txt"):
        new_filename = filename
        if filename.lower() == "GenrlTxt.txt".lower(): new_filename = "GENRLTX_.TXT"
        if filename.lower() == "Help.txt".lower(): new_filename = "Hel_.txt"
        correct_line_ending_and_adjustments(os.path.join("additional_files/translation/txt", filename), os.path.join("_tmp", new_filename), camp)
        files.append(os.path.join("_tmp", new_filename))
    command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + fn1] + files
    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
    for f in files: os.remove(f)

    command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + fn2] + ["_tmp/def/" + x for x in ["AVRcgen0.def", "AVRcgen1.def", "AVRcgen2.def", "AVRcgen3.def", "AVRcgen4.def", "AVRcgen5.def", "AVRcgen6.def", "AVRcgen7.def", "AVRcgn00.def", "AVRcgn01.def", "AVRcgn02.def", "AVRcgn03.def", "AVRcgn04.def", "AVRcgn05.def", "AVRcgn06.def", "AVRcgn07.def", "AVRcgn08.def", "AVWMON1.def", "AVWMON2.def", "AVWMON3.def", "AVWMON4.def", "AVWMON5.def", "AVWMON6.def", "AVWMON7.def", "AVWmrnd0.def", "AVZevnt0.def", "AVZGRAIL.def", "CamCusL.def", "CAMPCN.def", "CAMPLD.def", "CAMPRST.def", "CBBEGIB.DEF", "CBCANCB.DEF", "CBRESTB.DEF", "codefaul.def", "GSPBGIN.DEF", "GSPEXIT.DEF", "HISCCAM.def", "HiScExt.def", "HISCRES.DEF", "HISCSTA.def", "icm011.def", "icm012.def", "MuBjoin.def", "RanIsld.def", "RanNone.def", "RanNorm.def", "RanShow.def", "RanStrg.def", "RanWeak.def", "SCALBUT.DEF", "SCBUTT3.DEF", "SCNRBACK.def", "ScnrBeg.def", "ScnrExi.def", "SCNRLOD.DEF", "SCNRSAV.DEF", "SOLOAD.DEF", "SOMAIN.DEF", "SOQUIT.DEF", "SORETRN.DEF", "SORSTRT.DEF", "SOSAVE.DEF", "SYSOB12.DEF", "SYSOB13.DEF", "trrecb.def"]]
    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')


os.makedirs("_tmp/ChroniclesMod_patched/Data", exist_ok=True)
for filename in glob.glob(os.path.join("homm3_files/ChroniclesMod/Data", '*.*')):
    copy(filename, "_tmp/ChroniclesMod_patched/Data\\" + os.path.basename(filename))

copy(r"additional_files\translation\campaign\chronicles\Revolt of the Beastmasters.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
copy(r"additional_files\translation\campaign\chronicles\Tutorial_Bun.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Bun_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Bun_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Bun_bmE.lod", "Bun_spE.lod", 1)
copy(r"_tmp\chronicles\07_vid\Intro5.smk", "_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")
with open("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk", "r+b") as f: #entfernen der "anderen" Audiospuren
    f.seek(0x48)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
    f.seek(0x54)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Bun_E.VID"] + ["_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
#command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Bun_spE.lod"] + ["_tmp/chronicles/07_spr/" + s for s in os.listdir("_tmp/chronicles/07_spr/")]
#output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

copy(r"additional_files\translation\campaign\extra\WorldTree(dt).h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Drz_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Drz_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Drz_bmE.lod", "Drz_spE.lod", 2)

copy(r"additional_files\translation\campaign\chronicles\The Sword of Frost.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
copy(r"additional_files\translation\campaign\chronicles\Tutorial_Mie.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Mie_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Mie_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Mie_bmE.lod", "Mie_spE.lod", 3)
copy(r"_tmp\chronicles\08_vid\Intro6.smk", "_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")
with open("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk", "r+b") as f: #entfernen der "anderen" Audiospuren
    f.seek(0x48)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
    f.seek(0x54)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Mie_E.VID"] + ["_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

copy(r"additional_files\translation\campaign\extra\FieryMoon(dt).h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Ogn_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Ogn_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Ogn_bmE.lod", "Ogn_spE.lod", 4)

copy(r"additional_files\translation\campaign\chronicles\Conquest of the Underworld.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
copy(r"additional_files\translation\campaign\chronicles\Tutorial_Pod.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Pod_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Pod_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Pod_bmE.lod", "Pod_spE.lod", 5)
copy(r"_tmp\chronicles\02_vid\Intro.smk", "_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")
with open("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk", "r+b") as f: #entfernen der "anderen" Audiospuren
    f.seek(0x48)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
    f.seek(0x54)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Pod_E.VID"] + ["_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

copy(r"additional_files\translation\campaign\chronicles\Clash of the Dragons.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
copy(r"additional_files\translation\campaign\chronicles\Tutorial_Sza.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Sza_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Sza_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Sza_bmE.lod", "Sza_spE.lod", 6)
copy(r"_tmp\chronicles\04_vid\Intro.smk", "_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")
with open("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk", "r+b") as f: #entfernen der "anderen" Audiospuren
    f.seek(0x48)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
    f.seek(0x54)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Sza_E.VID"] + ["_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

copy(r"additional_files\translation\campaign\chronicles\Masters of the Elements.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
copy(r"additional_files\translation\campaign\chronicles\Tutorial_Wla.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Wla_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Wla_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Wla_bmE.lod", "Wla_spE.lod", 7)
copy(r"_tmp\chronicles\03_vid\Intro.smk", "_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")
with open("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk", "r+b") as f: #entfernen der "anderen" Audiospuren
    f.seek(0x48)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
    f.seek(0x54)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Wla_E.VID"] + ["_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

copy(r"additional_files\translation\campaign\chronicles\Warlords of the Wasteland.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
copy(r"additional_files\translation\campaign\chronicles\Tutorial_Woj.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Woj_bmE.lod"] + ["_tmp/fnt/" + s for s in os.listdir("_tmp/fnt")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Woj_bmE.lod"] + ["_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c", "_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')
patch("Woj_bmE.lod", "Woj_spE.lod", 8)
copy(r"_tmp\chronicles\01_vid\Intro.smk", "_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")
with open("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk", "r+b") as f: #entfernen der "anderen" Audiospuren
    f.seek(0x48)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
    f.seek(0x54)
    f.write(b'\0\0\0\0')
    f.write(b'\0\0\0\0')
command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Woj_E.VID"] + ["_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk"]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

os.remove("_tmp/ChroniclesMod_patched/Data\\" + "ab.h3c")
os.remove("_tmp/ChroniclesMod_patched/Data\\" + "Good1.h3c")
os.remove("_tmp/ChroniclesMod_patched/Data\\" + "NWCLOGO.smk")

command = ["tools/mmarch.exe", "add", "_tmp/ChroniclesMod_patched/Data/" + "Wsz_snE.snd"] \
    + ["_tmp/chronicles/01_snd/" + s for s in os.listdir("_tmp/chronicles/01_snd")] \
    + ["_tmp/chronicles/02_snd/" + s for s in os.listdir("_tmp/chronicles/02_snd")] \
    + ["_tmp/chronicles/03_snd/" + s for s in os.listdir("_tmp/chronicles/03_snd")] \
    + ["_tmp/chronicles/04_snd/" + s for s in os.listdir("_tmp/chronicles/04_snd")] \
    + ["_tmp/chronicles/0708_snd/" + s for s in os.listdir("_tmp/chronicles/0708_snd")]
output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0].decode('cp1252')

zipObj = ZipFile('_out/HoMM3DE_ChroniclesMod.zip', 'w', zipfile.ZIP_STORED)
for dirpath,dirs,files in os.walk("_tmp/ChroniclesMod_patched/Data\\"):
  for f in files:
    fn = os.path.join(dirpath, f)
    zipObj.write(fn, arcname=os.path.join("Data", f))
zipObj.close()