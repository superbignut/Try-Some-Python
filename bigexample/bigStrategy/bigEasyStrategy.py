from bigexample.bigCore import Strategy, SignalEvent
from queue import  Queue
from bigexample.bigData.bigCsvData import CsvDataHandler

import time

class EasyStrategy(Strategy):

    def __init__(self, event_queue, data_handler):
        self._event_queue = event_queue
        self._data_handler = data_handler

    def on_market_event(self, event):

        if event.type == "MARKET":

            current_data = self._data_handler.get_current_bar()
            print("### bigStrategy on_market_event ###", 'open price is: ', current_data['open'], time.ctime(time.time())[11:-5])

            signal_event = SignalEvent(symbol='IF', timestamp=time.time(), signal_direction=0)

            self._event_queue.put(signal_event) # 消耗 MARKET 生成 SIGNAL

if __name__ == '__main__':
    q = Queue()
    a = CsvDataHandler(event_queue=q, file_name='../local_data/IF.csv', duration=1)

    s = EasyStrategy(q, a)
    a.run()



