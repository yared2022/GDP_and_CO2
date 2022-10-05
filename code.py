import pandas as pd
import numpy as np

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
print(wdi.columns)
print(wdi.rows)
wdi_infant_mortality = wdi.loc[
    :,
    [
        "Country Name",
        "GDP per capita (constant 2010 US$)",
        "Mortality rate, infant (per 1,000 live births)",
    ],
]
