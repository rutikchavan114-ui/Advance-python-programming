import numpy as np
import pandas as pd

a=pd.Series(np.random.randint(1,101,10))

print("Series:")
print(a)

print("First:",a.iloc[0])
print("Above 50:")
print(a[a>50])

print("Mean:",a.mean())
print("Median:",a.median())
print("Min:",a.min())
print("Max:",a.max())
