import pandas as pd

bios = pd.read_csv("./data/bios.csv",engine='pyarrow',dtype_backend='pyarrow')
bios.info()
print(bios.sample(10))
