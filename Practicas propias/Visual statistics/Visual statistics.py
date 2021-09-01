import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import pandas_datareader.data as web


ticker = "KO"


def get_chart(ticker, initial_date, finish_date):
    return web.DataReader(ticker, "yahoo", initial_date, finish_date)


def get_EMA(info, periods):
    return info.ewm(span=periods).mean()


def get_MA(info, periods):
    return info.rolling(periods).mean()


def get_standard_deviation(info, periods):
    return info.ewm(span=periods).std()


def clasify_values(info, accuracy, volume):
    divide = (1.00001*(max(info))-min(info))/accuracy
    ranges = []
    frequency = []

    for d in range(accuracy):
        ranges.append(int(min(info)+d*divide))
        frequency.append(0)

    for d in range(len(info)):
        print(info[d])
        frequency[int((info[d] - min(info)) // divide)] += volume[d]

    return [ranges, frequency]


def main():
    chart = get_chart(ticker, dt.datetime(2015, 1, 1), dt.datetime(2021, 8, 30))
    chart["price_relation_change"] = chart["Close"]
    chart["EMA20"] = get_EMA(chart["Close"], 20)
    chart["EMA30"] = get_EMA(chart["Close"], 30)
    chart["Volume Flow"] = chart["Close"]


    for d in range(len(chart)):
        if d != 0:
            chart["price_relation_change"][d] = chart["Close"][d] / chart["Close"][d-1]

        else:
            chart["price_relation_change"][d] = 1

    for d in range(len(chart)):
        if chart["price_relation_change"][d] < 1:
            chart["Volume Flow"][d] = chart["Volume"][d] * -1
        else:
            chart["Volume Flow"][d] = chart["Volume"][d]


    chart["MACD"] = chart["EMA20"] / chart["EMA30"]
    chart["NEUTRAL"] = chart["Close"] - chart["Close"] + 1

    chart["EMA_CHANGE_20"] = get_EMA(chart["price_relation_change"], 20)
    chart["standard_deviation_20"] = get_standard_deviation(chart["Close"], 20)
    chart["Volume Flow EMA100"] = get_EMA(chart["Volume Flow"], 100)
    chart["Volume and Price"] = chart["Close"] * chart["Volume"]


    plots, ((price_change, EMA_CHANGE_20), (MACD, volume_flow_EMA), (standard_deviation, price),
            (volume_flow, volume_profile))\
        = plt.subplots(4, 2)
    price_change.plot(chart[["price_relation_change", "NEUTRAL"]])
    EMA_CHANGE_20.plot(chart[["EMA_CHANGE_20", "NEUTRAL"]])
    MACD.plot(chart[["MACD", "NEUTRAL"]])
    standard_deviation.plot(chart["standard_deviation_20"])
    volume_flow_EMA.plot(chart["Volume Flow EMA100"])
    price.plot(chart[["Close", "EMA20", "EMA30"]])
    volume_flow.plot(chart["Volume Flow"])
    volume_profile.hist(chart["Close"], 100)
    plt.show()


if __name__ == "__main__":
    main()