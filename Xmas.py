from datetime import datetime
from datetime import date
import time
while True:
    today = datetime.now()
    xmas = datetime(2021, 12, 24, 00, 00, 00)
    dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
    xmas_string = xmas.strftime("%d/%m/%Y %H:%M:%S")
    print("Ngày hiện tại là =", dt_string)
    print("Ngày Xmas là =", xmas_string)
    dt1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
    dt2 = datetime.strptime(xmas_string, "%d/%m/%Y %H:%M:%S")
    countXmas = dt2 - dt1
    print("Countdown to Xmas 2021: ",countXmas)
    time.sleep(5)
  