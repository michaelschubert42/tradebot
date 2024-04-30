import json

def speichere_json_kursdatei(symbol, json_data):
    file1 = open('kursdaten/' + symbol + '.json', 'w')
    file1.write(json.dumps(json_data))
    file1.close()

def lade_json_kursdatei(symbol):
    jsonFile = open('kursdaten/' + symbol + '.json', 'r')
    json_data =  json.load(jsonFile)
    jsonFile.close()
    return json_data