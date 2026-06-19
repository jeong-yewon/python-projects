import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.DataFrame( {
    "x":np.arange(10),
    "y":np.arange(10)*2+1
})

x = sm.add_constant(df["x"])
model = sm.OLS(df["y"], x).fit()

print(df)
print(model.summary())