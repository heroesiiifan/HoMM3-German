#Muss vor gemoddeten HotA ausgeführt werden -> Translate-Format Muss Englisch sein

#Händische nacharbeit bei Fehlern beim importieren (fehlende Zeilen) mit Beyond Compare -> Englisch/Deutsch
#+Für fehlendes: Offline DeepL (Textmarkieren Doppelt STRG+C -> übersetztes Einfügen)

import os
os.environ["PATH"] += ";C:\\" #Pfad der Treiber-Datei

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re
from copy import deepcopy
import sys

driver = webdriver.Firefox()
driver.get("https://www.deepl.com/translator")

def translate(input):
    if(input == ""): return ""
    elem = driver.find_element_by_class_name("lmt__source_textarea")
    while True:
        try:
            elem.clear()
            break
        except:
            pass
    elem.send_keys(input)
    elem.send_keys(Keys.RETURN)

    button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@dl-test=\"translator-source-lang-btn\"]")))
    ActionChains(driver).click(button).perform()

    button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@dl-test=\"translator-lang-option-en\"]")))
    ActionChains(driver).click(button).perform()

    button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@dl-test=\"translator-target-lang-btn\"]")))
    
    while True:
        try:
            ActionChains(driver).click(button).perform()
            button = WebDriverWait(driver, 2).until(ec.visibility_of_element_located((By.XPATH, "//button[@dl-test=\"translator-lang-option-de-DE\"]")))
            break
        except:
            pass
    ActionChains(driver).click(button).perform()

    time.sleep(0.3)

    while True:
        elem_res = driver.find_element_by_class_name("lmt__target_textarea")
        val = elem_res.get_attribute("value")
        time.sleep(0.2)
        if val != '' and val.find("[...]") == -1 and len(val) > 1: break
    time.sleep(1)
    val = elem_res.get_attribute("value")

    try:
        driver.find_element_by_class_name("lmt__target_textarea__proAd_text")
    except NoSuchElementException:
        pass
    else:
        raise ValueError('Too big Chunk')
        #val = "ERROR" + "\r\n\r\n###########################\r\n\r\n" + "ERROR" + "\r\n\r\n###########################\r\n\r\n" + "ERROR"

    while True:
        try:
            elem.clear()
            break
        except:
            pass

    return val

#print(translate("Hello World!"))

for dirpath,dirs,files in os.walk(r"C:\original_maps"):
    for f in files:
        fn = os.path.join(dirpath, f)

        if f.lower().endswith(".txt") and not os.path.isfile(fn.replace(".txt", ".translated")):
            hota = 0
            if f.lower().startswith("[hota]") : hota = 1

            f_ = open(fn, "r+b")
            content = f_.read()

            text = content.decode(encoding='cp1252')

            ext = 0
            if text.find("===== Heroes =====") != -1 : ext = 1

            sections = re.split("[\r\n]{0,4}===== .*? =====[\r\n]{2,6}", text, flags=re.M|re.S)

            map_name = sections[1]
            map_description = sections[2]
            map_rumors_name = [x.group(1) for x in re.finditer( r'Name:\r\n(.*?)\r\nText:', sections[3], flags=re.M|re.S)]
            map_rumors_text = [x.group(1) for x in re.finditer( r'Text:\r\n(.*?)(?=[\r\n]{2,6}Name:|\Z)', sections[3], flags=re.M|re.S)]
            map_timedevents_name = [x.group(1) for x in re.finditer( r'Name:\r\n(.*?)\r\nMessage:', sections[4], flags=re.M|re.S)]
            map_timedevents_message = [x.group(1) for x in re.finditer( r'Message:\r\n(.*?)(?=[\r\n]{2,6}Name:|\Z)', sections[4], flags=re.M|re.S)]
            map_objects = {smallItem.group(1):smallItem.group(2) for smallItem in re.finditer( r'(\([0-9].*?\*)\r\n(.*?)((?=\r\n\()|\Z)', sections[5+ext], flags=re.M|re.S)}
            for key, value in map_objects.items():
                map_objects[key] = {smallItem.group(1):smallItem.group(2) for smallItem in re.finditer( r'([^\r\n]{1,20}?):\r\n(.*?)\r{0,1}\n{0,1}(?=(?:\r\n[^\r\n]{1,20}?:|\Z))', value, flags=re.M|re.S)}

            
            new_map_name = deepcopy(map_name)
            new_map_description = deepcopy(map_description)
            new_map_rumors_name = deepcopy(map_rumors_name)
            new_map_rumors_text = deepcopy(map_rumors_text)
            new_map_timedevents_name = deepcopy(map_timedevents_name)
            new_map_timedevents_message = deepcopy(map_timedevents_message)
            new_map_objects = deepcopy(map_objects)

            translate_str = []
            translate_str.append(new_map_name)
            translate_str.append(new_map_description)
            for i in range(len(map_rumors_name)):
                translate_str.append(new_map_rumors_name[i])
                translate_str.append(new_map_rumors_text[i])
            for i in range(len(new_map_timedevents_name)):
                translate_str.append(new_map_timedevents_name[i])
                translate_str.append(new_map_timedevents_message[i])
            for key, value in new_map_objects.items():
                for key2, value2 in new_map_objects[key].items():
                    translate_str.append(new_map_objects[key][key2])

            def chunks(lst, n):
                """Yield successive n-sized chunks from lst."""
                for i in range(0, len(lst), n):
                    yield lst[i:i + n]
            translate_str_chunked = list(chunks(translate_str, 1)) #ggf. rumprobieren
            translated_str_unchunked = []
            for chunk in translate_str_chunked:
                translate_str = "\r\n\r\n###########################\r\n\r\n".join(chunk)
                translated_str_unchunked += translate(translate_str).replace("\n", "\r\n").split("\r\n\r\n###########################\r\n\r\n")
            for i in range(len(translated_str_unchunked)):
                translated_str_unchunked[i] = translated_str_unchunked[i].strip("\r\n").encode('latin1').decode('cp1252')
                
                
                
            new_map_name = translated_str_unchunked[0].replace("\r\n\r\n", "\r\n")
            new_map_description = translated_str_unchunked[1].replace("\r\n\r\n", "\r\n")
            j = 2
            for i in range(len(map_rumors_name)):
                new_map_rumors_name[i] = translated_str_unchunked[j].replace("\r\n\r\n", "\r\n")
                new_map_rumors_text[i] = translated_str_unchunked[j+1].replace("\r\n\r\n", "\r\n")
                j += 2
            for i in range(len(new_map_timedevents_name)):
                new_map_timedevents_name[i] = translated_str_unchunked[j].replace("\r\n\r\n", "\r\n")
                new_map_timedevents_message[i] = translated_str_unchunked[j+1].replace("\r\n\r\n", "\r\n")
                j += 2
            for key, value in new_map_objects.items():
                for key2, value2 in new_map_objects[key].items():
                    new_map_objects[key][key2] = translated_str_unchunked[j].replace("\r\n\r\n", "\r\n")
                    j += 1

            result = "===== Map name =====\r\n"
            result += new_map_name + "\r\n\r\n"
            result += "===== Map description =====\r\n"
            result += new_map_description + "\r\n\r\n"
            result += "===== Rumors =====\r\n\r\n"
            for i in range(len(map_rumors_name)):
                result += "Name:\r\n"
                result += new_map_rumors_name[i] + "\r\n"
                result += "Text:\r\n"
                result += new_map_rumors_text[i] + "\r\n\r\n"
            result += "===== Timed events =====\r\n\r\n"
            for i in range(len(new_map_timedevents_name)):
                result += "Name:\r\n"
                result += new_map_timedevents_name[i] + "\r\n"
                result += "Message:\r\n"
                result += new_map_timedevents_message[i] + "\r\n\r\n"
            if ext == 1: result += "===== Heroes =====\r\n\r\n"
            result += "===== Objects =====\r\n\r\n"
            for key, value in new_map_objects.items():
                result += key + "\r\n"
                for key2, value2 in value.items():
                    result += key2 + ":\r\n"
                    result += value2 + "\r\n"
                result += "\r\n"
            result += "===== End of file =====\r\n"


            fn = fn.replace(".txt", ".translated")
            with open(fn, 'w+b') as the_file:
                the_file.write(str.encode(result, encoding='cp1252'))
            pass

driver.close()