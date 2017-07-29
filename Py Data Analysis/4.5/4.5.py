from pandas import read_csv

import muyilib as my

df = read_csv(my.findpath_da("4.5\\data.csv"))

newName = df['name'].str.lstrip()

newName = df['name'].str.rstrip()

newName = df['name'].str.strip()

df['name'] = newName
