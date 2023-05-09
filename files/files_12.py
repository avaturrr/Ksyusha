"""Дан файл, содержащий различные даты.
 Каждая дата - это число, месяц и год. Найти самую раннюю дату."""

from csv_utils import *
from _datetime import datetime, timedelta
arr = [["2002-12-03"], ["1993-01-01"], ["2002-11-12"], ["2013-11-02"]]
write("my_csv_12.csv", arr)

dates = read("my_csv_12.csv")
delta_arr = []
for date in dates:
    date = datetime.strptime(date[0], "%Y-%m-%d")
    delta = int((datetime.now() - date).days)
    delta_arr.append(delta)

max_delta = max(delta_arr)
early_date = datetime.now() - timedelta(days=max_delta)

print(f"наиболее ранняя дата: {early_date}")
