import time
from RPA.Desktop.Windows import Windows
import os

mode = "IMPORT"

if mode == "EXPORT":
    #export
    win = Windows()

    win.open_executable("C:/HoMM3/h3maped.exe", "Map Editor", wildcard=True)
    for dirpath,dirs,files in os.walk("C:/original_maps"):
        for f in files:
            fn = os.path.join(dirpath, f).replace("/", "\\")

            if f.lower().endswith(".h3m") and not os.path.isfile(fn.replace(".h3m", ".txt")):
                hota = 0
                if f.lower().startswith("[hota]") : hota = 1

                if hota == 0:
                    while True:
                        try:
                            win.menu_select("File->Open...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%s")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    time.sleep(3)
                    while True:
                        try:
                            win.menu_select("File->Export Text...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%f")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}").replace(".h3m", ".txt") + "\"", send_delay=1, enter_delay=1)
                    time.sleep(3)
    win.close_all_applications()


    win.open_executable("C:/HoMM3/h3hota_maped.exe", "Map Editor", wildcard=True)
    for dirpath,dirs,files in os.walk("C:/original_maps"):
        for f in files:
            if f.lower().endswith(".h3m"):
                hota = 0
                if f.lower().startswith("[hota]") : hota = 1

                fn = os.path.join(dirpath, f).replace("/", "\\")

                if hota == 1:
                    win.menu_select("File->Open...")
                    win.send_keys("%n")
                    time.sleep(0.2)
                    win.send_keys_to_input("\"" + fn.replace(" ", "{SPACE}") + "\"", send_delay=0.2)
                    win.menu_select("File->Export Text...")
                    win.send_keys("%n")
                    time.sleep(0.2)
                    win.send_keys_to_input("\"" + fn.replace(" ", "{SPACE}").replace(".h3m", ".txt") + "\"", send_delay=0.2)
    win.close_all_applications()

if mode == "IMPORT":
    #import
    win = Windows()

    win.open_executable("C:/HoMM3/h3maped.exe", "Map Editor", wildcard=True)
    for dirpath,dirs,files in os.walk("C:/original_maps"):
        for f in files:
            fn = os.path.join(dirpath, f).replace("/", "\\")
            fn_map = os.path.join(dirpath, f).replace("/", "\\").replace(".translated", ".h3m")
            fn_new = os.path.join(dirpath + "/out", f).replace("/", "\\").replace(".translated", ".h3m")

            if f.lower().endswith(".translated") and not os.path.isfile(fn_new):
                hota = 0
                if f.lower().startswith("[hota]") : hota = 1

                if hota == 0:
                    while True:
                        try:
                            win.menu_select("File->Open...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%s")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn_map.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    time.sleep(3)
                    while True:
                        try:
                            win.menu_select("File->Import Text...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%f")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    try:
                        win.find_element("partial name:Successfully")
                        win.send_keys("{ENTER}")
                    except:
                        print(fn_new)
                        win.send_keys("{ENTER}")
                        continue
                    time.sleep(3)
                    while True:
                        try:
                            win.menu_select("File->Save As...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%f")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn_new.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    time.sleep(3)
    win.close_all_applications()


    win.open_executable("C:/HoMM3/h3hota_maped.exe", "Map Editor", wildcard=True)
    for dirpath,dirs,files in os.walk("C:/original_maps"):
        for f in files:
            fn = os.path.join(dirpath, f).replace("/", "\\")
            fn_map = os.path.join(dirpath, f).replace("/", "\\").replace(".translated", ".h3m")
            fn_new = os.path.join(dirpath + "/out", f).replace("/", "\\").replace(".translated", ".h3m")

            if f.lower().endswith(".translated") and not os.path.isfile(fn_new):
                hota = 0
                if f.lower().startswith("[hota]") : hota = 1

                if hota == 1:
                    while True:
                        try:
                            win.menu_select("File->Open...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%s")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn_map.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    time.sleep(3)
                    while True:
                        try:
                            win.menu_select("File->Import Text...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%f")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    try:
                        win.find_element("partial name:Successfully")
                        win.send_keys("{ENTER}")
                    except:
                        print(fn_new)
                        win.send_keys("{ENTER}")
                        continue
                    time.sleep(3)
                    while True:
                        try:
                            win.menu_select("File->Save As...")
                            break
                        except:
                            time.sleep(2)
                            win.send_keys("%f")
                    win.send_keys("%n")
                    time.sleep(1)
                    win.send_keys_to_input("\"" + fn_new.replace(" ", "{SPACE}").replace("(", "{(}").replace(")", "{)}") + "\"", send_delay=1, enter_delay=1)
                    time.sleep(3)
    win.close_all_applications()

pass