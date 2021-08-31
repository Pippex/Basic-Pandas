import matplotlib.pyplot as plt
import pandas as pd
import datetime
import pandas_datareader.data as web


def get_chart(ticker, initial_date, finish_date):
    return web.DataReader(ticker, "yahoo", initial_date, finish_date)


def get_MA(info, periods):
    return info.rolling(periods).mean()


def get_EMA(info, periods):
    return info.ewm(span=periods).mean()


def empty_column(info):
    return info[list(info)[3]] - info[list(info)[3]]


def substract_dataframe(dataframe1, dataframe2):
    return dataframe1 - dataframe2


def divide_dataframe(dataframe1, dataframe2):
    return (dataframe1/dataframe2) ** 150


def main():
    AMZN = get_chart("AMZN", datetime.datetime(2015, 1, 1), datetime.datetime(2020, 8, 28))

    AMZN["EMA20"] = get_EMA(AMZN["Close"], 20)
    AMZN["EMA30"] = get_EMA(AMZN["Close"], 30)
    AMZN["EMASIGNAL"] = empty_column(AMZN)
    AMZN["MACDSIGNAL"] = empty_column(AMZN)
    AMZN["MACD"] = divide_dataframe(AMZN["EMA20"], AMZN["EMA30"])

    for d in range(len(AMZN["EMA20"])):
        if d+1 < len(AMZN["EMA20"]):

            if AMZN["EMA20"][d] < AMZN["EMA30"][d]:
                if AMZN["EMA20"][d+1] > AMZN["EMA30"][d+1]:
                    AMZN["EMASIGNAL"][d+1] = AMZN["EMA30"][d]/10

            if AMZN["EMA20"][d] > AMZN["EMA30"][d]:
                if AMZN["EMA20"][d + 1] < AMZN["EMA30"][d + 1]:
                    AMZN["EMASIGNAL"][d + 1] = AMZN["EMA30"][d]/(-10)

    for d in range(len(AMZN["MACD"])):
        if AMZN["MACD"][d] ** (1/150) >= 1.05:
            AMZN["MACDSIGNAL"] = AMZN["Close"]/10

    plt.plot(AMZN["Close"], label="AMZN")
    plt.plot(AMZN["EMA20"], label="EMA 20")
    plt.plot(AMZN["EMA30"], label="EMA 30")
    plt.plot(AMZN["EMASIGNAL"], label="EMA SIGNAL")
    plt.plot(AMZN["MACD"], label="MACD")
    plt.plot(AMZN["MACDSIGNAL"], label="MACD SIGNAL")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()