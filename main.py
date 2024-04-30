from kursverzeichnis import *

kursdaten_json = lade_json_kursdatei('MBG')

class Json_Kursdaten:
    def __init__(self, kursdaten_json):
        self.kursdaten = kursdaten_json


    def tagesdaten_fuer_datum(self, datum):
        tageskursdaten = self.kursdaten['Time Series (Daily)']
        if tageskursdaten.get(datum):
            return ohlc_aus_json(tageskursdaten[datum])
        return OHLC(0, 0, 0, 0)
    
class OHLC:
    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def __repr__(self):
        return f'open: {self.open}, high: {self.high}, low: {self.low}, close: {self.close}'

def ohlc_aus_json(ohlc_json):
    open = ohlc_json['1. open']
    high = ohlc_json['2. high']
    low = ohlc_json['3. low']
    close = ohlc_json['4. close']
    return OHLC(float(open), float(high), float(low), float(close))


kursdaten = Json_Kursdaten(kursdaten_json)
print(kursdaten.tagesdaten_fuer_datum('2024-04-30'))
