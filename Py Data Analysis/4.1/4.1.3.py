from pandas import read_excel;

import muyilib as my

df = read_excel(my.findpath_da("4.1//3.xlsx"),
    sheetname='data'
)
df