import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas_datareader.data as web


def get_chart(ticker, initial_date, finish_date):
    return web.DataReader(ticker, "yahoo", initial_date, finish_date)


def get_MA(info, periods):
    return info.rolling(periods).mean()


def get_EMA(info,periods):
    return info.ewm(span=periods).mean()


def empty_column(info):
    return info[list(info)[3]] - info[list(info)[3]]


AMZN = get_chart("AMZN",datetime.datetime(2015, 1, 1),datetime.datetime(2020, 8, 28))

AMZN["EMA20"] = get_EMA(AMZN, 20)
AMZN["EMA30"] = get_EMA(AMZN, 30)
AMZN["SIGNAL"] = empty_column(AMZN)

for d in range(len(AMZN["EMA20"])):
    if d+1 < len(AMZN["EMA20"]):

        if AMZN["EMA20"][d] < AMZN["EMA30"][d]:
            if AMZN["EMA20"][d+1] > AMZN["EMA30"][d+1]:
                AMZN["SIGNAL"][d+1] = 1

        if AMZN["EMA20"][d] > AMZN["EMA30"][d]:
            if AMZN["EMA20"][d + 1] < AMZN["EMA30"][d + 1]:
                AMZN["SIGNAL"][d + 1] = -1

print(AMZN["SIGNAL"])

plt.plot(AMZN["Close"], label="AMZN")
plt.plot(AMZN["SIGNAL"], label = "Signal")
plt.show()