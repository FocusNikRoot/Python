import numpy as np

table = np.genfromtxt(
    r'ABBREV.csv',
    delimiter=';',
    names=True,
    dtype=None,
    encoding="utf8"
)

names = table['Shrt_Desc']

max_cal = np.max(float(Kcal) for Kcal in table['Energ_Kcal'])
print(max_cal)