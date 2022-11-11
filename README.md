# Heroes3-German
Inoffizielle deutsche Übersetzung von Heroes III Complete Edition für VCMI / H3HD / HotA / Chronicles.

## Nutzung
### [HoMM3 Complete](https://www.gog.com/game/heroes_of_might_and_magic_3_complete_edition)
* Dateien z.B. mit [MMArchive](https://github.com/GrayFace/Misc/) austauschen (nicht näher beschrieben -> nutzt Google).

### [VCMI](https://vcmi.eu/)
* Installation über den in VCMI integrierten Mod-Manager: [German translation](https://github.com/vcmi-mods/german-translation)

Alternativ:
* VCMI-Paket in Mods-Ordner (z.B. Mods/HoMM3_GER) extrahieren.

### [HoMM3 HD](https://sites.google.com/site/heroes3hd/)
* HD-Paket in "Heroes of Might and Magic III/_HD3_Data/Packs" (z.B. Packs/German) extrahieren.
* Die #de.ini in "Heroes of Might and Magic III/_HD3_Data/Lang" kopieren.
* Die cham.fnt in "Heroes of Might and Magic III/_HD3_Data/Common" kopieren.
* Kampagnen in Maps-Ordner kopieren

### [HotA](https://www.hota.acidcave.net/)
* Bei HotA die HotA.dat, HotA_ext.lod und HotA_l_ext.lod austauschen
* Maps in den Maps-Ordner kopieren

### [Chronicles Mod](https://www.moddb.com/mods/heroes-chronicles-fully-compability-hdmod)
* Dateien in Data-Folder nach kompletter Installation extrahieren (Englisch ist dann Deutsch)

## Was braucht man?
* Man muss im Besitz von Heroes 3 Complete sein (Retail oder GOG) -> Bitte besorgt euch die Originale, kostet ja fast nix mehr. 🙂
* 7-ZIP zum entpacken

## Bauen
* Benötigt Complete 4.0 / Heroes III RoE in Deutsch / HotA 1.6.1 / Heroes III SoD in Deutsch / Chronicles in Deutsch -> Dateien müssen kopiert werden, siehe "homm3_files/benoetigt.txt"
* Chronicles Mod für VCMI - https://wiki.vcmi.eu/Mod_list (umgewandelt in ZIP)
* Die build.py mit Python 3 starten (requirements.txt müssen via pip installiert werden).
* Buildvorgang läuft aktuell nur unter Windows (case not sensitive & EXEn).
* 7-ZIP sollte installiert (und in %PATH%) sein

## Kompatibilität (getestet)
* Heroes III Complete 4.0
* Heroes III HD mod 5.4 RC7
* Heroes III Horn of the Abyss 1.6.1
* VCMI 1.0
* [SOD_SP](https://github.com/RoseKavalier/H3Plugins/releases)
* Heroes Chronicles - Fully Compability HDmod 2.5.8

## Was Fehlt?
* Audio/Video von AB und HotA in Deutsch
* Originale AB-Kampagnen/-Szenarien in Deutsch (wurde offiziell nie übersetzt)
* Todo: siehe Backlog

## Vorgehensweise: HoMM3 HD frisch installieren
* Complete installieren
* HD-Mod installieren
* Data-CD in den Ordner "CD data"
* #de.ini kopieren in lang
* Dateien aus Zip in "Packs/German"
* Ggf. [SOD_SP](https://github.com/RoseKavalier/H3Plugins/releases) installieren (in INI-Datei von "eng" auf "deu" ändern)
* Heroes Chronicles-Kampagnen in den Maps-Ordner kopieren
* Sprache im Menü auf Deutsch umstellen & Mod hinzufügen
* genießen

Anleitungsvideo mit GOG-Version, HD, HotA und Deutsch-Patch:
[Video](doc/install_h3_hd_hota_ger.webm)

## Zusatzmodule
* [mmarch.exe](https://github.com/might-and-magic/mmarch)
* [HotA editor.exe](http://imperium.heroes.net.pl/temat/4762/1)
* [splitter.exe](https://forum.df2.ru/lofiversion/index.php/t933-50.html)

## Backlog / Todo
Achtung: Übersetzungen in Textdateien in Kodierung CP1252 (in Notepad++: ANSI), NICHT UTF-8!!!

## Hauptspiel
* Datum bei der Szenarienauswahl in Englisch (nur Hauptspiel, nicht HotA - da passt es)
* Bessere (?) Übersetzungen für DeepL-konvertierte Maps (AB)

### HotA
* SpTraits.txt ggf. noch von DeepL optimieren
* Bessere (?) Übersetzungen für DeepL-konvertierte Maps

### Chronicles Mod
* Launcher (in .NET geschrieben; mit "dnlib" sollten sich Strings/Ressourcen anpassen lassen)
* Aufwendig gestaltete Buttons (z.B. "Play", aber auch "New Game") -> gibts teilweise in den deutschen Ressourcen (müssen aber ggf. neu positioniert werden)
* Texte bei der Kampagnenauswahl
* Kampagnen Einführungen (Bilder) -> nicht in den Ressourcen vorhanden?!
* "The Glory of War"

### ggf. [Sucession Wars](https://www.moddb.com/mods/h3sw)
* Komplett zu übersetzen

## Changelog
### TBD
* CSSexit.def korrigiert -> Im Kampagnenbildschirm wird nun "Zurück" angezeigt (für VCMI irrelevant)

### 1.9.2
* Szenarientitel angepasst
* Chronicles Mod: Videos
* Tutorials der Chronicles

### 1.9.1
* Unterstützung für die Chronicles Mod

### 1.9
* HD Übersetzung angepasst
* HotA-Editor vervollständigt (Danke an: Darktobas)
* neue VCMI Texte übersetzt
* angepasste VCMI-Beschreibung

### 1.8
* HD: NoToLower-Mod zum unterbinden der Kleinschreibung bei Ressourcen [H3-Plugins](https://github.com/RoseKavalier/H3Plugins) ([License](https://github.com/RoseKavalier/H3Plugins/blob/master/LICENSE))

### 1.7
* kleine Übersetzung-Fixes
* Encoding-Fixes
* original Maps, Kampagnen, ein paar Sprites und Audio aus offiziellem, deutschem SoD

### 1.6
* Ctrl in Strg umbenannt
* SOD_SP Übersetzung
* HotA Kampagnen mit [DeepL](https://www.deepl.com/translator) übersetzt
* HotA DAT-Texte übersetzt
* Fehlende TXT ergänzt

### 1.5
* loadgame.bmp, newgame.bmp und Kampagnenhintergrund in HD
* Originaltexte der dt. Übersetzung bei RoE-Kampagne

### 1.4
* HotA Data-Übersetzung (teilw. optimiertes DeepL)
* HotA Diff-Texte Übersetzung
* DEF-Icons
* Diverse Fixes
* Schrift im Haupfenster (HD) - Umlaute

### 1.3
* Übersetzungen der Einzelspieler-Szenarien durch [DeepL](https://www.deepl.com/translator)
* SoD Kampagnen Einleitungstexte auf Deutsch.
* VCMI Bonus-Texts (mit DeepL)
* HotA-Texte adaptiert (HotA-Änderungen mit deutschen Übersetzung gemischt)

### 1.2
* Bilder / Icons in HotA
* Offizielle Chronicles Kampagnen Übersetzung hinzugefügt
* Chronicles-Addon für VCMI deutsch gemodded

### 1.1
* Initialer Release