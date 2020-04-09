from multiprocessing import Process, Queue
import read_in
import trade
"""
print("Current Bitcoin price: ", read_in.price, "        Change in the last 24h:", read_in.change, "%",
              "        Absolut change: ", read_in.absolute_change[:5],
              "$", "        Change in last second: ", read_in.change_second[:6], "%", "        Current High: ", read_in.current_high, "$")

if float(read_in.price_float) > read_in.current_high:
    print("BUY!")
"""