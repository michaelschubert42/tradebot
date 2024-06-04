from kursverzeichnis import *
from Json_Kursdaten import Json_Kursdaten

kursdaten_json = lade_json_kursdatei('MBG')

kursdaten = Json_Kursdaten(kursdaten_json)
print(kursdaten.tagesdaten_fuer_datum('2024-04-29'))
