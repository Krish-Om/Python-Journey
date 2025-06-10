import pandas as pd

bios = pd.read_csv("./data/bios.csv")


print(bios.sample(10))
