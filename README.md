# Heroes3-German
Deutsche Übersetzung von Heroes III Complete Edition für VCMI / H3HD / HotA.

## Nutzung
### [HoMM3 Complete](https://www.gog.com/game/heroes_of_might_and_magic_3_complete_edition)
Dateien z.B. mit [MMArchive](https://github.com/GrayFace/Misc/) austauschen (nicht näher beschrieben -> nutzt Google).

### [VCMI](https://vcmi.eu/)
VCMI-Paket in Mods-Ordner (z.B. Mods/HoMM3_GER) extrahieren.

### [HoMM3 HD](https://sites.google.com/site/heroes3hd/)
HD-Paket in "Heroes of Might and Magic III/_HD3_Data/Packs" (z.B. Packs/German) extrahieren.
Die #de.ini in "Heroes of Might and Magic III/_HD3_Data/Lang" kopieren.

### [HotA](https://www.hota.acidcave.net/)
Bei HotA die HotA.dat, HotA.lod und HotA_lng.lod austauschen

## Was braucht man?
* Man muss im Besitz von Heroes 3 Complete sein (Retail oder GOG) -> Bitte besorgt euch die Originale, kostet ja fast nix mehr. 🙂
* 7-ZIP zum entpacken

## Bauen
* Benötigt Complete 4.0 / Heroes III RoE in Deutsch / HotA 1.6.1 / Chronicles in Deutsch -> Dateien müssen kopiert werden, siehe "homm3_files/benoetigt.txt"
* Chronicles Mod für VCMI - https://wiki.vcmi.eu/Mod_list (umgewandelt in ZIP)
* Die build.py mit Python 3 starten (requirements.txt müssen via pip installiert werden).
* Buildvorgang läuft aktuell nur unter Windows (case not sensitive & EXEn).
* 7-ZIP sollte installiert (und in %PATH%) sein

## Kompatibilität (getestet)
* Heroes III Complete 4.0
* Heroes III HD mod 5.2 RC17
* Heroes III Horn of the Abyss 1.6.1
* VCMI 0.99 (f31c516)

## Was Fehlt?
* Singleplayer-Maps + Audio/Video von AB und SoD in Deutsch
* Todo: siehe Backlog

## Vorgehensweise: HoMM3 HD frisch installieren
* Complete installieren
* HD-Mod installieren
* Data-CD in den Ordner "CD data"
* #de.ini kopieren in lang
* Dateien aus Zip in "Packs/German"
* (die vier (Beastmasters(dt).h3c, FieryMoon(dt).h3c, FrostSword(dt).h3c & WorldTree(dt).h3c) Heroes Chronicles-Kampagnen aus dem Packs-Ordner in den Maps-Ordner kopieren)
* Sprache im Menü auf Deutsch umstellen & Mod hinzufügen
* genießen

## Zusatzmodule
* [mmarch.exe](https://github.com/might-and-magic/mmarch)
* [HotA editor.exe](http://imperium.heroes.net.pl/temat/4762/1)

## Backlog
Achtung: Übersetzungen in Textdateien in Kodierung CP1252 (in Notepad++: ANSI), NICHT UTF-8
### Allgemein
* deutsche Singleplayer-Szenarien von SoD + deutsche Kampagnenbeschreibung (via Kampagneneditor) + deutsches Audio/Video (Kein deutsches SoD vorhanden -> selten)
* Icons erstellen
  * CSSCUS.DEF
  * CSSEXIT.DEF
  * CSSROE.DEF
  * CSSSOD.DEF
  * GTBACK.DEF
  * GTCAMPN.DEF
  * GTMULTI.DEF
  * GTSINGL.DEF
  * GTTUTOR.DEF
  * MMENUCR.DEF
  * MMENUHS.DEF
  * MMENULG.DEF
  * MMENUNG.DEF
  * MMENUQT.DEF
  * RANISLD.DEF
  * RANNONE.DEF
  * RANNORM.DEF
  * RANSHOW.DEF
  * RANSIZL.DEF
  * RANSIZM.DEF
  * RANSIZS.DEF
  * RANSIZX.DEF
  * RANSTRG.DEF
  * RANWEAK.DEF
  * SCNRNEX.DEF
  * CBBACKB.DEF
  * CORETRN.DEF
  * SCALBUT.DEF
  * SCNRMPSZ.DEF
### VCMI
* bonus_texts.json übersetzen
### HD
* Newgame & Loadgame werden nicht ersetzt?
* SoD-Kampagne Background in Deutsch!
### HotA
* (TODO) Diff Texte zwischen hota/de/alt und hota/de/neu erzeugen (z.B. mit WinMerge)
  * hota/de/neu übersetzen (auf Basis von Vergleich hota/en/neu zu hota/en/neu)
* Bitmaps
  * icm0110.pcx
  * icm0111.pcx
  * icm0112.pcx
  * icm0120.pcx
  * icm0121.pcx
  * icm0122.pcx
  * loadgame.pcx
  * newgame.pcx
* Sprites
  * avrcgn09.def
  * avzaren0.def
  * avzaren1.def
  * avzaren2.def
  * avzaren3.def
  * Main-Menü-Icons (für HotA)
* (TODO) .DAT übersetzen (hota/txt)
* Szenarien / Kampagnen
* Bug?: Katapult in Burg kaufen Text

## Changelog
### 1.2
* Bilder / Icons in HotA
* Offizielle Chronicles Kampagnen Übersetzung hinzugefügt
* Chronicles-Addon für VCMI deutsch gemodded

### 1.1
* Initialer Release