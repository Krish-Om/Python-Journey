import pandas as pd
import math


NTC = pd.read_csv(
    "./nepse-dataset/data/NTC_2000-01-01_2021-12-31.csv",
    engine="pyarrow",
    dtype_backend="pyarrow",
)
# ### Consistency of Close price


if "__name__" == "main":
    NTC_close_price = NTC["Close Price"].copy()
    count_close_price = NTC_close_price.count()
    sum_close_price = NTC_close_price.sum()


    mean = float(sum_close_price / (count_close_price))


    NTC_SUM_SQUARE = 0
    for x in NTC_close_price:
        NTC_SUM_SQUARE += x**2

    diff = float((NTC_SUM_SQUARE - (mean**2)) / count_close_price)

    SD = math.sqrt(diff)

## Coefficent of Variation
    CV = (SD / mean) * 100
