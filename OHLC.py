class OHLC:
    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def __repr__(self):
        return f'open: {self.open}, high: {self.high}, low: {self.low}, close: {self.close}'