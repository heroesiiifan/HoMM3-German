import gzip
import os

for x in range(0, 8):
    if os.path.exists('_tmp/chronicles/0' + str(x+1) + '_camp/Main.h3c'):
        f=gzip.open('_tmp/chronicles/0' + str(x+1) + '_camp/Main.h3c','rb')
        file_content=f.read()
        parts = file_content.split(b'\x1D\x00\x00\x00\x01')

        ct = 0
        for y in parts:
            if ct > 0:
                f = gzip.open('_tmp/chronicles/0' + str(x+1) + '_camp/Main0' + str(ct) + '.h3m', 'wb')
                f.write(b'\x1C\x00\x00\x00\x01' + y) #Inklusive Version "Downgrade"
                f.close()
            ct += 1

pass

# Weiteres Vorgehen:
# -> deutsche Texte mit Mapeditor extrahieren ("Export Text...")
# -> Kampagnen-Editor aus englischen Kampagnen Szenarien extrahieren
# -> deutsche Texte in extrahierte Szenarien importieren (bei zwei musste durch einen deutsch-englisch Vergleich Hand angelegt werden)
# -> Kampagnen-Editor -> Szenarien importieren
# -> Kampagnen-Editor -> englische Texte exportieren
# -> Deutsche V7 Kampagnen mit 7zip entpacken, dann mit Notepad++ Strings rauskopieren und in englische Exports einfügen
# -> Angepassten Texte wieder einlesen