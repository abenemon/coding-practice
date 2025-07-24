import pandas as pd
df = pd.read_csv("FrenchSpanishEnglishVerbsFrCommon.csv")

print(df[df["French"].str.endswith("re") & df["French"].str.startswith("a")])