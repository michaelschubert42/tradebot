from OHLC import OHLC

class Json_Kursdaten:
    def __init__(self, kursdaten_json):
        self.kursdaten = kursdaten_json

    def tagesdaten_fuer_datum(self, datum):
        tageskursdaten = self.kursdaten['Time Series (Daily)']
        if tageskursdaten.get(datum):
            return self.ohlc_aus_json(tageskursdaten[datum])
        return OHLC(0, 0, 0, 0)
    
    def ohlc_aus_json(self, ohlc_json):
        open = ohlc_json['1. open']
        high = ohlc_json['2. high']
        low = ohlc_json['3. low']
        close = ohlc_json['4. close']
        return OHLC(float(open), float(high), float(low), float(close))